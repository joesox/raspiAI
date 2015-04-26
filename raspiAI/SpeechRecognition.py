import os
import sys
import speech_recognition as sr
from dragonfly.all import Grammar, CompoundRule

__version__ = '0.1.20150419'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "SpeechRecognition Class to work with SpeechRecognitionAPI."

class SpeechRecognition(object):
    """description of SpeechRecognition class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def HearWAVfiledemo (self):
        r = sr.Recognizer()
        with sr.WavFile("ilikepie.wav") as source:          # use "ilikepie.wav" as the audio source
            audio = r.record(source)                        # extract audio data from the file

        try:
            print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
        except LookupError:                                 # speech is unintelligible
            print("Could not understand audio")

    def Micinput (self):
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

        try:
            print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")

# Voice command rule combining spoken form and recognition processing.
class ExampleRule(CompoundRule):
    spec = "do something computer"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        print "Voice command spoken."


def demo():
    c = SpeechRecognition()
    c.HearWAVfiledemo()
    print "Finished SpeechRecognition demo!"

def demo2():
    r = SpeechRecognition()
    r.Micinput()
    print "Finished SpeechRecognition demo!"
 
def demo3():
    # Create a grammar which contains and loads the command rule.
    grammar = Grammar("example grammar")                # Create a grammar to contain the command rule.
    grammar.add_rule(ExampleRule())                     # Add the command rule to the grammar.
    grammar.load()                                      # Load the grammar. 

if __name__ == '__main__':
  demo()
