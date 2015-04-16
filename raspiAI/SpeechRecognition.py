import os
import sys
import speech_recognition as sr

__version__ = '0.1.20150415'
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

def demo():
    c = SpeechRecognition()
    c.HearWAVfiledemo()
    print "Finished SpeechRecognition demo!"

if __name__ == '__main__':
  demo()
