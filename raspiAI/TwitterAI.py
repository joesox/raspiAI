from TwitterAPI import TwitterAPI
import time
__version__ = '0.1.20150418'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI. Update your C:\Python27\Lib\site-packages\\twitterapi-2.3.3-py2.7.egg\TwitterAPI\credentials.txt"
__localcreds__ = 'C:\Python27\Lib\site-packages\\twitterapi-2.3.3-py2.7.egg\TwitterAPI\credentials.txt'
"""
Twitter supports both user and application authentication, known as oAuth 1 and oAuth 2:
-User authentication gives you access to all API endpoints, basically read and write persmission. 
-Application authentication gives you access to just the read portion of the API ? so, no creating or destroying tweets. 
-Application authentication also has elevated rate limits.
"""
class TwitterAI(object):
    """
    Twitter Class to work with TwitterAPI
        credentialsfile = path to credentials.txt in Python site-packages-twitterapi-2.3.3-py2.7.egg
    """
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def __init__(self, credentialsfile):
        """
        credentialsfile = path to credentials.txt in Python site-packages-twitterapi-2.3.3-py2.7.egg
        Initialize global class variables
        """
        try:
            """
            loadsettings() reads the credentialsfile.txt installed with TwitterAPI module
            consumer_key=
            consumer_secret=
            access_token_key=
            access_token_secret=
            """
            self.lineList = open(credentialsfile, 'r').readlines()
            for i, line in enumerate(self.lineList):
                splitlist = line.split('=')
                if(splitlist[0] == "consumer_key"):
                    self.consumer_key = splitlist[1].strip("\n")
                if(splitlist[0] == "consumer_secret"):
                    self.consumer_secret = splitlist[1].strip("\n")
                if(splitlist[0] == "access_token_key"):
                    self.access_token_key = splitlist[1].strip("\n")
                if(splitlist[0] == "access_token_secret"):
                    self.access_token_secret = splitlist[1].strip("\n")
        except NameError, x:
            print 'Exception: ', x

    def PostTweet(self, text):
        """
        PostTweet(text)
            text = Text to post to twitter
        """
        api = TwitterAPI(self.consumer_key,
                 self.consumer_secret,
                 self.access_token_key,
                 self.access_token_secret)
        r = api.request('statuses/update', {'status': text})
        #print('PostTweet SUCCESS' if r.status_code == 200 else 'PostTweet FAILURE')
        if (r.status_code == 200):
            return True
        else:
            print("Status code: " + r.text)
            return False

def demo():
    tweets = TwitterAI(__localcreds__)
    TESTTOSEND = "Demo version PostTweet test version: " + __version__ + str(time.time())
    print("SENDING: " + TESTTOSEND)
    #perform tweet...
    result = tweets.PostTweet(TESTTOSEND)
    if(result == True):
        print("\r\nPostTweet SUCCESS!")
    else:
        print("\r\nPostTweet FAILURE!")
    print "Finished TwitterAI demo!"

def demoTwo():
    tweets = TwitterAI(__localcreds__)
    TESTTOSEND = raw_input("ENTER WHAT TO SEND: ")
    print("SENDING: " + TESTTOSEND)
    #perform tweet...
    result = tweets.PostTweet(TESTTOSEND)
    if(result == True):
        print("\r\nPostTweet SUCCESS!")
    else:
        print("\r\nPostTweet FAILURE!")
    print "Finished TwitterAI demo!"

if __name__ == '__main__':
  demo()

