import requests
import os
import time
import datetime
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
from html import unescape

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


bugun = datetime.date.today()
aylar = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
bu_ay = aylar[bugun.month]
bu_gun = bugun.day
hashtag = f"{{{bu_gun} {bu_ay}}} > #TarihteBugün"
# print(hashtag)

def strip_tags(html):
    return unescape(BeautifulSoup(html, 'html.parser').text)

def tweekibot():
    try:
        wiki = requests.get('https://tr.wikipedia.org/wiki/Vikipedi:Tarihte_bug%C3%BCn')
        wiki_page = wiki.text
        soup = BeautifulSoup(wiki_page, 'html.parser')

        ul_elements = soup.find_all('ul')

        if len(ul_elements) >= 2:
            second_ul = ul_elements[-9]
            list_items = second_ul.find_all('li')

            # Liste öğelerini tersine çevir
            list_items.reverse()
            
            tweet_list = []

            for counter, line in enumerate(list_items):
                if counter == 5:
                    break
                tweet = strip_tags(str(line))
                tweet_list.append(tweet)

            return tweet_list

    except Exception as e:
        print("Error while scraping Wikipedia:", e)
        return []

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

tweet_list = tweekibot()
tweet = "\n".join(tweet_list)  # Tweet listesini tek bir dizede birleştir

for tweet in tweet_list:
    payload = {"text": f"{tweet}\n\n{hashtag}"}

    print("Payload: %s" % payload)

    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    
    if response.status_code != 200:
        print("Request returned an error: {} {}".format(response.status_code, response.text))
    else:
        print("Tweet sent successfully")

    time.sleep(20)  # 20 saniyelik aralık
