#!/usr/bin/python

import tweepy
import config
import json

class StdOutListener(tweepy.StreamListener):
  def on_data(self, data):
    tweet = json.loads(data)
    print '------------------------------------------'
    print tweet['text']
  def on_error(self, status):
    print status

def startStream(track):
  global stream
  stream.filter(track=[track], async=True)
def stopStream():
  global stream
  stream.disconnect()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
stream = tweepy.Stream(auth, StdOutListener())

def main():
  track = raw_input('Welcome! What is the word filter to obtain Tweets?\n')
  startStream(track)
  raw_input('Press any key to stop the stream\n')
  stopStream()

if __name__ == '__main__':
  main()
