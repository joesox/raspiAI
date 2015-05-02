import os
import requests
from chatterbotapi import ChatterBotFactory, ChatterBotType
__version__ = '0.1.20150502'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI. "
__raspiaibotid__ = "f3d034f13e34d592"

class Pandorabot(object):
    """ Description of Pandorabot class raspiai Pandorabot: http://www.pandorabots.com/pandora/talk?botid=f3d034f13e34d592 """
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def __init__(self, botid):
        """
        Initialize global class variables
        Create aiml object with file
        """
        try:
            self._factory = ChatterBotFactory()
            self._bot = self._factory.create(ChatterBotType.PANDORABOTS, __raspiaibotid__)
            self._botsession = self._bot.create_session()
        except NameError, x:
            print 'Exception: ', x

def demo():
    P = Pandorabot(__raspiaibotid__)
    print P._botsession.think("Hello")
    print P._botsession.think("What is your name?")
    print "Finished Pandorabot demo!"

if __name__ == '__main__':
  demo()

"""
////////////////////
///    HELP FAQ  ///
////////////////////
=== How to train your pandorabot to handle "my name is *" ===
1) Sign into the Pandorabot website and click on your Pandorabot, then click on the Train link
2) In the textbox, type the sentence "MY NAME IS *" then click "Ask" button.
3) When the results comeback, Click Advanced Alter Response button
4) In the pattern textbox, make sure "MY NAME IS *" (without the quotations) looks like
MY NAME IS *
5) In the template textbox place the following:
Hello !
6) Click Submit button
7) Then click on your Pandorabot's name link
8) Click republish or your training will not be live.
"""
