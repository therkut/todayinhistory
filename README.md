# Generating Daily Tweets from Wikipedia

This project retrieves updates from Wikipedia and utilizes them for sharing on Twitter. Below, you can find how the code works and how to configure it.

## Steps

1. **Downloading Required Libraries:**

   As the first step, include the following Python libraries in your project. These libraries are essential for data retrieval, posting tweets to Twitter, and data processing.

   - `os`: Used for file operations and accessing environment variables.
   - `time`: Used for time delays.
   - `datetime`: Used for date and time operations.
   - `requests`: Used for making HTTP requests.
   - `html`: Used for cleaning HTML tags.
   - `bs4` (Beautiful Soup): Used for parsing and extracting content from HTML documents.
   - `requests_oauthlib`: Used for communication with the Twitter API using OAuth authentication.

2. **Defining Constants:**

   Define the constant values used in the project. These constants include:

   - `WIKIPEDIA_URL`: URL used for fetching data from Wikipedia.
   - `TWITTER_API_URL`: URL for making requests to the Twitter API.
   - `WAIT_INTERVAL`: The wait time between each tweet (in seconds).
   - `TD_ELEMENT_ID`: The ID of the `td` element on the Wikipedia page that contains updates.

3. **Twitter API Authentication:**

   To communicate with the Twitter API, you need to authenticate. Authenticate by providing the following information:

   - `consumer_key`: Twitter API consumer key.
   - `consumer_secret`: Twitter API consumer secret.
   - `access_token`: Twitter API access token.
   - `access_token_secret`: Twitter API access token secret.

4. **Get Today's Date and Create a Hashtag:**

   The code obtains today's date and creates a hashtag in the Turkish date format.

5. **Create a Function for Stripping HTML Tags:**

   Define a function called `strip_tags`. This function removes HTML tags and converts the content into plain text.

6. **Retrieve Wikipedia Data:**

   The `get_wikipedia_data` function retrieves data from Wikipedia. This function fetches and cleans updates from the Wikipedia page.

7. **Create a Tweet Posting Function:**

   The function named `post_tweet` sends the specified tweet text to Twitter. The tweet posting function communicates with the Twitter API and checks the status of the sent tweet.

8. **Create the Main Function:**

   The main function, `main`, retrieves Wikipedia data, generates tweets, and posts them to Twitter. It provides a delay with the specified waiting time between each tweet.

9. **Run the Code:**

   To run the code, call the `main` function using the `if __name__ == '__main__':` block. This allows the code to run automatically.

## Usage

This project can be used to automatically fetch daily updates and share them on Twitter. Before using it, you'll need to configure your Twitter API credentials and other requirements. Follow the steps below to run the project:

1. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 requests_oauthlib
   ```

2. Set your Twitter API credentials:

   - `CONSUMER_KEY`
   - `CONSUMER_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_TOKEN_SECRET`

3. Run the code:

   ```bash
   python main.py
   ```

The code will fetch updates from Wikipedia and share them on Twitter with the specified waiting interval.

## License

This project is licensed under the MIT License. For more information, refer to the LICENSE file.
