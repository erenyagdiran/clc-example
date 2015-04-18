#!/usr/bin/python 

import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
api.update_status(status='Hello, world!')

def newTweet():
  tweet = raw_input('Welcome! What would you like to tweet?\n')
  try:
    api.update_status(status=tweet)
    print 'Tweeted succesfully!'
  except tweepy.TweepError as e:
    print e


if __name__ == '__main__':
  newTweet()
