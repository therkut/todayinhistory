import os
import time
import datetime
import requests
from html import unescape
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session

# Constants
WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Main_Page'
TWITTER_API_URL = 'https://api.twitter.com/2/tweets'
WAIT_INTERVAL = 40  # 40-second interval
TD_ELEMENT_ID = 'mp-itn'  # ID of the td element

# Twitter API credentials
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


# Get today's date and create a hashtag with Turkish date format
today = datetime.date.today()
months = ["", "Ocak - January", "Şubat - February", "Mart - March", "Nisan - April", "Mayıs - May", "Haziran - June", "Temmuz - July", "Ağustos - August", "Eylül - September", "Ekim - October", "Kasım - November", "Aralık - December"]
this_month = months[today.month]
this_day = today.day
hashtag = f"{this_day} {this_month} > #Today #Date #Current #Information #OnThisDay"

# Authenticate with Twitter API
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# Function to fetch Wikipedia data and create a reusable session
def get_wikipedia_data():
    session = requests.Session()  # Create a reusable session
    try:
        response = session.get(WIKIPEDIA_URL)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        wiki_page = response.text
        soup = BeautifulSoup(wiki_page, 'html.parser')

        td_tag = soup.find('td', {'id': TD_ELEMENT_ID})
        ul_tag = td_tag.find('ul')
        li_tags = ul_tag.find_all('li')
        li_tags.reverse()

        tweet_list = [strip_tags(li.get_text()) for li in li_tags[:5]]
        return tweet_list
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data from Wikipedia:", str(e))
        return []
    finally:
        session.close()  # Close the session to release resources

# Function to strip HTML tags from text
def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

# Function to post a tweet
def post_tweet(tweet_text):
    try:
        payload = {"text": tweet_text}
        response = oauth.post(TWITTER_API_URL, json=payload)
        response.raise_for_status()
        print("Tweet sent successfully:", tweet_text)
    except Exception as e:
        print("Request returned an error: {} {}".format(response.status_code, response.text))

# Main function
def main():
    # Get Wikipedia data and post tweets
    tweet_list = get_wikipedia_data()
    for tweet in tweet_list:
        tweet_text = f"{tweet}\n\n{hashtag}"
        post_tweet(tweet_text)
        time.sleep(WAIT_INTERVAL)

if __name__ == '__main__':
    main()
