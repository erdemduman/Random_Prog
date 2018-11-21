import tweepy
import link_generator
import time
import account_info
import mention_stream
import logs
import signal
import os

authenticate = tweepy.OAuthHandler(account_info.consumer_key, account_info.consumer_secret)
authenticate.set_access_token(account_info.access_token, account_info.access_token_secret)
api = tweepy.API(authenticate, wait_on_rate_limit=True)

postTime = 11

log = logs.Log('out.log')
link = link_generator.LinkGenerator(log)
myStreamListener = mention_stream.MyStreamListener(api, log, link)
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@' + account_info.account_user_name + " prog"], async=True)

def signal_handler(signal, frame):
    log.debug("Keyboard Interrupt.")
    log.close()
    os._exit(1)

def postTweet(api, postTime):

    while(True):
        if(int(time.strftime('%M')) == postTime):
            send = link.chooseTrack()
            try:
                api.update_status(status=send)
            except tweepy.TweepError:
                postTweet(api, postTime)

            if(postTime != 0):
                postTime -= 1
            else:
                postTime = 59


signal.signal(signal.SIGINT, signal_handler)
postTweet(api, postTime)