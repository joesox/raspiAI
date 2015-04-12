import os
import sys
__version__ = '0.1.20150412'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "SpeechRecognition Class to work with SpeechRecognitionAPI."

class SpeechRecognition(object):
    """description of SpeechRecognition class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

def demo():
    c = SpeechRecognition()
    print "Finished SpeechRecognition demo!"

if __name__ == '__main__':
  demo()
