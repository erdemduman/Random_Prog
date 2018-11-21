import tweepy
import link_generator

class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api, log, link):
        super(MyStreamListener, self).__init__()
        self.__api = api
        self.__log = log
        self.__link = link

    def on_status(self, status):
        if not status.retweeted:
            self.mention_tweet(status)
    
    def on_error(self, status_code):
        if status_code == 420:
            self.__log.error("Mention error is here.")
            return False
    
    def mention_tweet(self, dest):
        send = self.__link.chooseTrack()
        try:
            self.__api.update_status("@" + str(dest.user.screen_name) + " " + str(send), dest.id)
        
        except tweepy.TweepError:
            self.mention_tweet(dest)
            