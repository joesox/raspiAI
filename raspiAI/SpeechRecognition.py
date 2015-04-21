import os
import sys
import speech_recognition as sr

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

    def MicinputDemo (self):
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        try:
            print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
        except LookupError:                            # speech is unintelligible
            print("Could not understand audio")

    def Micinput (self):
        r2 = sr.Recognizer()
        with sr.Microphone() as source2:               # use the default microphone as the audio source
            audio2 = r2.listen(source2)                   # listen for the first phrase and extract it into audio data
        try:
            return str(r2.recognize(audio2))    # recognize speech using Google Speech Recognition
        except LookupError:                            # speech is unintelligible
            return ""

def demo():
    c = SpeechRecognition()
    c.HearWAVfiledemo()
    print "Finished SpeechRecognition demo!"

def demo2():
    r = SpeechRecognition()
    r.MicinputDemo()
    print "Finished SpeechRecognition demo!"
     

if __name__ == '__main__':
  demo2()
