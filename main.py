from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy.error import RateLimitError
from datetime import datetime, date, timedelta
from collections import Counter
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

ACCESS_TOKEN = "Coucou"
ACCESS_TOKEN_SECRET = "Coucou"
API_KEY = "Coucou"
API_SECRET_KEY = "Coucou"

def get_twitter_usernames():
    return [
        "EmmanuelMacron",
        "murielpenicaud",
        "pyduan",
        "Cyrilhanouna",
        "rudygobert27",
        "MLP_officiel",
        "benoithamon",
        "JLMelenchon",
        "UrbanLePharaon"
    ]

def main():
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(auth)
    df = pd.DataFrame()
    for user in get_twitter_usernames():
        df1 = pd.DataFrame()
        previous_id_last = -1
        id_last = -2
        total_tweets_user = []
        while len(total_tweets_user) < 3000 and previous_id_last != id_last:
            try:
                if id_last != -2:
                    tweets = api.user_timeline(user, max_id = id_last, tweet_mode='extended')
                else:
                    tweets = api.user_timeline(user, tweet_mode='extended')
            except RateLimitError:
                print("Rate limit exceeded, lets wait for 15 minutes")
                time.sleep(15*60)
                if id_last != -2:
                    tweets = api.user_timeline(user, max_id = id_last, tweet_mode='extended')
                else:
                    tweets = api.user_timeline(user, tweet_mode='extended')
            for tweet in tweets:
                tweet_text = tweet.full_text
                #if "https://t.co/" in tweet_text:
                #    tweet_text = tweet_text.split('https://t.co')[0]
                if tweet_text.startswith("RT"):
                    continue
                total_tweets_user.append(tweet_text)
            previous_id_last = id_last
            id_last = tweets[-1].id
            print(f"User : {user} - Nb tweets : {len(total_tweets_user)} - id_last : {id_last} - previousid_last : {previous_id_last}")
        df1 = df1.assign(tweets=total_tweets_user)

        #Save single user CSV
        df1.to_csv(f"output/csv/tweets_{user}-{date.today()}.csv", sep='|', index=False, encoding="utf-8")
        df1.to_pickle(f"output/pickle/tweets_{user}-{date.today()}.pickle")

        #Save all tweets into one file
        df = pd.concat([df,df1], ignore_index=True, axis=1)
        df.columns = get_twitter_usernames()[0:len(df.columns)]
        df.to_csv(f"output/csv/ALL_TWEETS-{date.today()}.csv", sep='|', index=False, encoding="utf-8")
        df.to_pickle(f"output/pickle/ALL_TWEETS-{date.today()}.pickle")

if __name__ == '__main__':
    main()


