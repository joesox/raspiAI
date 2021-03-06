import os
import sys
import pyttsx
__version__ = '0.1.20150410'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Text-to-Speech class that handles basic Text-to-Speech functions."
__here__ = os.path.abspath(os.path.dirname(__file__))

class txttospeech(object):
    """
    Text-to-Speech class that handles
    basic Text-to-Speech functions.
    """
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)
    
    def __init__(self, rate, voicenum):
        """ Initalize all global variables needed """
        self.Rate = rate
        self.engine = pyttsx.init()                             # ## Set up the voice engine ##
        self.engine.setProperty('rate', self.Rate)
        self.voices = self.engine.getProperty('voices')
                                                                #Check to make sure voicenum variable is a number before assigning to array
        if (isinstance( voicenum, ( int, long ) )):
            self.Voice = self.voices[voicenum]
        else:
            self.Voice = self.voices[0]
        self.engine.setProperty('voice', self.Voice.id)

    """ 
    Sends the text to the txttospeech engine 
    if True, send to print    
    """
    def Say(self, text, bPrint):
        #Did we want to display this speech in text on screen?
        #important: print before saying so we have something to read right away
        if (bPrint == True):
            print text
        self.engine.say(text)
        self.engine.runAndWait()

def demo():
    speech = txttospeech(90, 0)
    print "Started!"
    speech.Say("Listen up! I am speaking!", True)
    print "Finished txttospeech demo!"
    print "**************"

if __name__ == '__main__':
  demo()


