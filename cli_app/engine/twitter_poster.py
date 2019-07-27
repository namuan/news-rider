import os
import sys
from dotenv import load_dotenv
import tweepy
from .log_helper import logger

sys.path.append(os.getcwd())
load_dotenv(verbose=True)

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def send_tweet(tweet):
    if len(tweet) > 140:
        logger.warn(f"Ignoring {tweet} because the size of message({len(tweet)}) > 140")
    else:
        logger.info(f"Sending tweet {tweet}")
        api.update_status(tweet)
