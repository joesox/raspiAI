import os
import sys
import aiml
__version__ = '0.1.20150419'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "AIML Class to work with AIML."

class AIMLAI(object):
    """description of AIML class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

def Say(self, input, aimlkernel):
    """ Take incoming sentence and guide a properly learned response using AIML """
    aimlkernel.__class__= aiml.Kernel
    rawresponse = ""
    #<jist_subj_events>[['What', "be today 's weather"]]</jist_subj_events>
    # Get a raw response from loaded AIML
    rawresponse = aimlkernel.respond(input)
        
    # If AIML returns "WARNING: No match found for input" then this object does not know how to respond back
    #BOOLVAL = rawresponse.startswith("WARNING: No match found for input")
    if(rawresponse == ""):
        rawresponse = "I DON'T UNDERSTAND"#or '??'
    return rawresponse

#def demo():
#    AIMLEngine = AIMLAI("aiml-en-us-foundation-alice\default.aiml")
#    AIMLEngine.say("my name is joe")
#    print "Finished AIML demo!"

#if __name__ == '__main__':
#  demo()