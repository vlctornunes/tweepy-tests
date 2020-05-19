import tweepy as tw
import pandas as pd

with open('to-do.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

#public_tweets = api.home_timeline()

search_words = 'Whinderson' + '-filter:retweets'
public_tweets = tw.Cursor(api.search, q=search_words).items(30)

for tweet in public_tweets:
    print(tweet.source)