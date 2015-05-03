#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import sched, time
import TXT2SPEECH
import TwitterAI
import random
__version__ = '0.1.20150502'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Jokes Class: Tells jokes when asked to and when something triggers it to speak it."
__localcreds__ = 'C:\Python27\Lib\site-packages\\twitterapi-2.3.3-py2.7.egg\TwitterAPI\credentials.txt'
#http://www.rd.com/jokes/funny/
## TO DO:   -ADD MORE JOKES
##          -MAKE SURE TELL ALL JOKES FIRST B4 TELLING AGAIN

class Jokes(object):
    """description of Jokes class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def TellRandomJoke(self, bTxt2spch, bTweet, bTweetConfirmation):
        """ 
        TellRandomJoke(bTxt2spch, bTweet, bTweetConfirmation)
        Tells first part of joke then pauses then completes joke. 
            If bTxt2spch = True then will use TXT2Speech
            If bTweet = True then tweet joke
            If bTweetConfirmation = then print if success or fail
        """
        #Load the JOKES!:P!:P!:
        jokes = list(["What's the best thing about Switzerland?|Not sure, but the flag is a big plus."])
        jokes += list(["MapQuest really needs to start its directions on number five. Pretty sure I know how to get out of my neighborhood."])
        jokes += list(["For Christmas, I gave my kid a BB gun. He gave me a sweater with a bullseye on the back."])
        jokes += list(["I bet cats have a secret website where they upload clips of cute humans trying to open DVD packaging and jump-start cars."])

        #pick the random joke now, just get it over with
        JOKE = random.sample(jokes, 1)
        JOKE = str(JOKE).decode('utf8')

        #Is there a pipe in the text? if so then its a two-part joke with external interaction
        #   if not, then just do a one-liner
        if (str(JOKE).find("|") == -1):
            if(bTxt2spch == False):
                #NO TEXT TO SPEECH SO JUST PRINT JOKES
                # tell joke      
                print str(JOKE).strip()
            else:
                mouth = TXT2SPEECH.txttospeech(100, 0)
                # tell joke
                text1 = str(JOKE).strip()
                mouth.Say(text1, True)
                #ARE WE TWEETING THIS JOKE?
                if (bTweet == True):
                    self.TweetJoke(text1, bTweet, bTweetConfirmation)
        else:
            #A PIPE WAS FOUND, TWO-PART JOKE
            if(bTxt2spch == False):
                #NO TEXT TO SPEECH SO JUST PRINT JOKES
                # tell first part of joke                       : Whats the best thing about Switzerland?
                print str(str(jokes[0]).split('|')[0]).strip().decode('utf8')
                # prompt the user for any input, just ignore
                s = sched.scheduler(time.time, time.sleep)
                raw_input("ANY RESPONSE? > ")
                time.sleep(2)
                # Rell rest of joke                             : Not sure, but the flag is a big plus.
                print str(str(jokes[0]).split('|')[1]).strip().decode('utf8')
                # Play random laugh
            else:
                mouth = TXT2SPEECH.txttospeech(100, 0)
                # tell first part of joke                       : Whats the best thing about Switzerland?
                text1 = str(str(jokes[0]).split('|')[0]).strip().decode('utf8')
                mouth.Say(text1, True)
                # prompt the user for any input, just ignore
                s = sched.scheduler(time.time, time.sleep)
                raw_input("ANY RESPONSE? > ")
                time.sleep(2)
                # Rell rest of joke                             : Not sure, but the flag is a big plus.
                text2 = str(str(jokes[0]).split('|')[1]).strip().decode('utf8')
                mouth.Say(text2, True)
                # Play random laugh
                mouth.Say("Ha HAA ha. Woooha", True)
                #ARE WE TWEETING THIS JOKE?
                if (bTweet == True):
                    self.TweetJoke(text1 + "|" + text2, bTweet, bTweetConfirmation)


    def TweetJoke(self, text, bTxt2spch, bConfirmation):
        """
        TweetJoke(text, bTxt2spch, bConfirmation)
            text = Text to post to twitter
            If bTxt2spch = True then will use TXT2Speech
            If bTweetConfirmation = then print if success or fail
        """
        twitter = TwitterAI.TwitterAI(__localcreds__)
        result = twitter.PostTweet(text)

        if (bTxt2spch == True):
            mouth = TXT2SPEECH.txttospeech(100, 0)
            mouth.Say(text, True)

        if(bConfirmation == True):
            if(result == True):
                print("\r\nPostTweet SUCCESS!")
            else:
                print("\r\nPostTweet FAILURE!")

def demo():
    Jokes().TellRandomJoke(True, False, False)
    print "Finished Jokes demo!"

def demo2():
    Jokes().TellRandomJoke(True, True, True)
    print "Finished Jokes demo!"

if __name__ == '__main__':
  demo()