# You will need to install tweepy==3.8  using PIP or in PyCharm for this to work and will also need to create a Twitter API account.
# Run this on your own machine
# You need to register with Twitter/X in order to use this Twitter Bot script
# A free account isn't sufficient as the functionality below allows you to pull data - which isn't covered under their free version

import tweepy
import time

# The data below will be unique to your own account after requesting access to the Twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
# prints your name
print(user.name)
# prints your screen name
print(user.screen_name)
# prints your follow count
print(user.followers_count)

# Add whatever keyword you'd like to search in the quotations
search = ""

# You can change the value here to whatever you'd like
numberOfTweets = 5


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            # 1 second "pause" so that you don't hit the Twitter request limit
            time.sleep(1000)


# This lets you follow someone within your follower list if their username comes up
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    # add someone's username here
    if follower.name == 'username':
        print(follower.name)
        follower.follow()


# Like your own tweets. or retweet anything with a keyword using the search string variable above
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
