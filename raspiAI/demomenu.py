import TXT2SPEECH
import TwitterAI
import SpeechRecognition
import Vision

__version__ = '0.1.20150415'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = 'Demo Menu for raspiAI'

def printline(length, div, line):
    """
        Print a line of length <length> with a * at each end and <line> in the body
        <div> determins where the line should be justified
        1 right justified
        2 centered
        use any large number for left
    """
    pad = max(0, (length-len(line))/div)
    print "*%*s%-*s *" %(pad+1, ' ', length-pad, line)

def box(length, justify, *lines):
    """
        Disaply <lines> in a box of *'s width <length>
        Split each line at < >  if to long
        Justify gives the overall text justification
            c: center
            r: right
            default left
    """
    div = {'c':2, 'r':1}.get(justify, 100)
    print "*"*(length+4)
    for line in lines:
        if len(line) <= length or ' ' not in line:
            printline(length, div, line)
        else: 
            store = ''
            for word in line.split():
                if len(store)+len(word)+1 > length:
                    printline(length, div, store.strip())
                    store = ''
                store = store+' '+word
            printline(length, div, store.strip())
    print "*"*(length+4)

def run_menu(width, values, *options):
    """
        Create a menu of width <width> from a tuple of one description, function/method per option
        Add an exit method at the end of the list
        Display with each option being given an integer key in order starting from 1
        Repeatedly ask for an option and call the linked function untill asked to stop
        The menu can also be left by entering 'exit'
    """
    while True:
        tmp = ['%i) %s'%(i+1, s[0]%values) for i, s in enumerate(options)]
        box(width, 'l', 'Choose one of the below:', *tmp+['%i) exit'%(len(options)+1)])
        entered = raw_input("> ")
        try:
            choice = int(entered)
        except:
            if(str(entered).lower() == "exit"):
                break
        else:
            if choice == len(options)+1:
                break
            elif 0 < choice <= len(options):
                options[choice-1][1]()

class demomenu(object):
    """ """
    def _txttospeech(self):
        """ Demo TXT2SPEECH """
        tts = TXT2SPEECH.demo()

    def _twitterauto(self):
        """ Demo TwitterAI [PostTweet-auto]"""
        twitter = TwitterAI.demo()

    def _twitterprompt(self):
        """ Demo TwitterAI [PostTweet-prompt]"""
        twitter = TwitterAI.demoTwo()

    def _speechrecognition(self):
        """ Demo speechrecognition"""
        sr = SpeechRecognition.demo()

    def _visionphoto(self):
        """ Demo Vision class """
        v = Vision.demo()

    def menu(self):
        """Main Menu loop"""
        box(40, 'c', 'raspiAI', __version__, __url__, '-'*40, __doc__)
        run_menu(40, self.__dict__, 
                ('Text2Speech demo', self._txttospeech),
                ('Twitter [PostTweet-auto] demo', self._twitterauto),
                ('Twitter [PostTweet-prompt] demo', self._twitterprompt),
                ('SpeechRecognition demo', self._speechrecognition),
                ('Vision demo [photo]', self._visionphoto))

def start():
    i = demomenu()
    i.menu()

if __name__ == '__main__':
    start()