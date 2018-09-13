import tweepy 
import link_generator

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api

    def on_status(self, status):
        if not status.retweeted:
            self.mention_tweet(status)
    
    def on_error(self, status_code):
        if status_code == 420:
            print("Mention error is here.")
            return False
    
    def mention_tweet(self, dest):
        send = link_generator.chooseTrack()
        try:
            self.api.update_status("@" + str(dest.user.screen_name) + " " + str(send), dest.id)
        
        except tweepy.TweepError:
            self.mention_tweet(dest)
            