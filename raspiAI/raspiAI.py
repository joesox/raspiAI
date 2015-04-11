import os
import sys
import pyttsx
__version__ = '0.1.20150410'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Text-to-Speech class that handles basic Text-to-Speech functions."
__here__ = os.path.abspath(os.path.dirname(__file__))
"""
[TEXT2SPEACH]
 Text-to-Speech class that handles
 basic Text-to-Speech functions.
"""
class TXT2SPEECH:
    """
    Text-to-Speech class that handles
    basic Text-to-Speech functions.
    """
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)
    
    """ Initalize all global variables needed """
    def __init__(self, rate, voicenum):
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
    Sends the text to the TXT2SPEECH engine 
    if True, send to print    
    """
    def Say(self, text, bPrint):
        self.engine.say(text)
        self.engine.runAndWait()
        #Did we want to display this speech in text on screen?
        if (bPrint == True):
            print text

def start():
    speech = TXT2SPEECH(90, 1)
    print "Started!"
    speech.Say("Listen up! I am speaking!", True)
    print "Finished!"
    print "**************"

if __name__ == '__main__':
  start()