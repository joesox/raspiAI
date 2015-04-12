#from TwitterAPI import TwitterAPI
#__version__ = '0.1.20150412'
#__author__ = "JPSIII and sjs_20012001"
#__url__ = 'https://github.com/joesox/raspiAI'
#__doc__ = "Twitter Class to work with TwitterAPI."

#"""
#Twitter supports both user and application authentication, known as oAuth 1 and oAuth 2:
#-User authentication gives you access to all API endpoints, basically read and write persmission. 
#-Application authentication gives you access to just the read portion of the API ? so, no creating or destroying tweets. 
#-Application authentication also has elevated rate limits.
#"""
#class TwitterAI(object):
#    """Twitter Class to work with TwitterAPI"""
#    def __repr__(self):
#        if not self:  
#            return 'Attrs()'  
#        return '<%s>' % (self.__class__.__name__)

#    def __init__(self, consumerkey, consumersecret, accesstokenkey, accesstokensecret):
#        """ Initialize global class variables """
#        self.consumer_key = consumerkey
#        self.consumer_secret = consumersecret
#        self.access_token_key = accesstokenkey
#        self.access_token_secret = accesstokensecret


#    def PostTweet(self, text):
#        api = TwitterAPI(self.consumer_key,
#                 self.consumer_secret,
#                 self.access_token_key,
#                 self.access_token_secret)
#        r = api.request('statuses/update', {'status': text})
#        #print('PostTweet SUCCESS' if r.status_code == 200 else 'PostTweet FAILURE')
#        if (r.status_code == 200):
#            return True
#        else:
#            return False

#def demo():
#    #tweets = TwitterAI(_CONSUMERKEY, _CONSUMERSECRET, _ACCESSTOKENKEY, _ACCESSTOKENSECRET)
#    tweets = TwitterAI("25enA89NntEbLNOjRkVVfghQN", "AVfN70sGHszyhPY9wPFuiPnmoGxKdsQUCXc6wGfFdiaU5epR4p", "3150477894-cqpOY8FDfUn7xu84TfQ3lCoVqgIsM5OKlzyaUGG", "cPpEpYKIDR7XU0kh18Xy7MkcZkDYQjoNfhusAlknno3tj")
#    TESTTOSEND = "Demo version PostTweet test version: " + __version__
#    print("SENDING: " + TESTTOSEND)
#    #perform tweet...
#    result = tweets.PostTweet(TESTTOSEND)
#    if(result == True):
#        print("\r\nPostTweet SUCCESS!")
#    else:
#        print("\r\nPostTweet FAILURE!")
#    print "Finished TwitterAI demo!"

#def demoTwo():
#    tweets = TwitterAI(_CONSUMERKEY, _CONSUMERSECRET, _ACCESSTOKENKEY, _ACCESSTOKENSECRET)
#    TESTTOSEND = "Demo version PostTweet test version: " + __version__
#    print("SENDING: " + TESTTOSEND)
#    #perform tweet...
#    result = tweets.PostTweet(TESTTOSEND)
#    if(result == True):
#        print("\r\nPostTweet SUCCESS!")
#    else:
#        print("\r\nPostTweet FAILURE!")
#    print "Finished TwitterAI demo!"

#if __name__ == '__main__':
#  demo()

