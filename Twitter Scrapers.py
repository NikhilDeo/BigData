# -*- coding: utf-8 -*-
"""
Nikhil Deo
Big Data
Twitter Scraper - Code from socialmedia-class.org
"""
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '454507265-FFqUsBw0YFuR6Hu9VV4UmH6H1d62e3JNcF3OLor7'
ACCESS_SECRET = 'QAMP7p3XcTqURFj7XIak8RaVgv9BoijakfPoZibwHQHAA'
CONSUMER_KEY = 'BVCorqDHCRABUMhuyndjkhHeO'
CONSUMER_SECRET = 'wcDX2gS4awtfziWUZ0Oh06zVjfgxGYDM36Zo7Hj8mLM4qeIoOg'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

data = twitter.search.tweets(geocode = '47.676819,-122.374872,1mi', count = 100, until = '2016-05-31')
with open('twitter_rest_sample', 'w') as outfile:
    json.dump(data, outfile)

# We use the file saved from last step as example
tweets_filename = 'twitter_rest_sample'
tweets_file = open(tweets_filename, "r")

obj = open('tweetDataBallardHS.txt', 'w', encoding = 'utf8')

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        for x in range(100):
            tweet_line = ''
            if 'text' in tweet['statuses'][x]: # only messages contains 'text' field is a tweet
               tweet_line+=str(tweet['statuses'][x]['id'])# This is the tweet's id
               tweet_line+=','
               tweet_line+=(tweet['statuses'][x]['text'])# Text of tweet
            tweet_line+='\n'
            obj.write(tweet_line)
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue

obj.close()