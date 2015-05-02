import os
import sys
import speech_recognition as sr
import thread
import time

__version__ = '0.1.20150502'
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

    def callback(recognizer, audio):                          
        """ this is called from the background thread """
        try:
            print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
        except LookupError:
            print("Oops! Didn't catch that")
        r = sr.Recognizer()
        r.listen_in_background(sr.Microphone(), callback)

    #def ListenRealTime(self):
        #launch a seperate listening thread to constantly listen for someone talking
        #thread.start_new_thread( callback, (, 2, ) )

def demo():
    c = SpeechRecognition()
    c.HearWAVfiledemo()
    print "Finished SpeechRecognition demo!"

def demo2():
    r = SpeechRecognition()
    r.Micinput()
    print "Finished SpeechRecognition demo!"

def demo3():
    r = SpeechRecognition()


if __name__ == '__main__':
  demo3()
