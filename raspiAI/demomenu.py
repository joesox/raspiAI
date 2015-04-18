import os
import sys
import TXT2SPEECH
import TwitterAI
import SpeechRecognition
import Vision
import Jokes
import AIMLAI
import aiml
__version__ = '0.1.20150416'
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
    def __init__(self, aimlfile):
        """
        Initialize global class variables
        Create aiml object with file
        """
        self.AIMLFILE = aimlfile
        self._k = aiml.Kernel()
        #self._k.bootstrap(learnFiles = aimlfile)
        #self._k.saveBrain("raspiai.brn")   
        full_file_paths = self.get_filepaths("aiml-en-us-foundation-alice")
        self._k.bootstrap(learnFiles = full_file_paths)

    def get_filepaths(self, directory):
        """
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
        """
        file_paths = []  # List which will store all of the full filepaths.

        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

        return file_paths  # Self-explanatory.

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

    def _visionvideo(self):
        """ Demo Vision class """
        v = Vision.demo2()

    def _tellrandomjoke(self):
        """ Demo Joke class """
        j = Jokes.demo()

    def _tellrandomjokeandtweet(self):
        """ Demo Joke class """
        j = Jokes.demo2()

    def _aimldemo(self):
        """ Demo Joke class """
        print "RUNNING PRE-SET TESTS..."
        #Tell who you are
        print "INPUT:My name is Joe.|OUTPUT:" + AIMLAI.Say(self, "My name is Joe.", self._k)
        #who
        print "INPUT:What is your name?|OUTPUT:" + AIMLAI.Say(self, "What is your name?", self._k)
        #what
        print "INPUT:What is your purpose?|OUTPUT:" + AIMLAI.Say(self, "What is your purpose?", self._k)
        #when
        print "INPUT:When where you born?|OUTPUT:" + AIMLAI.Say(self, "When where you born?", self._k)
        #why
        print "INPUT:Why are you here?|OUTPUT:" + AIMLAI.Say(self, "Why are you here?", self._k)
        print "INPUT:What is your favorite hobby?|OUTPUT:" + AIMLAI.Say(self, "What is your favorite hobby?", self._k)
        print "INPUT:Do you know Ben?|OUTPUT:" + AIMLAI.Say(self, "Do you know Ben?", self._k)
        print "INPUT:Do you know Joe?|OUTPUT:" + AIMLAI.Say(self, "Do you know Joe?", self._k)
        print "=====\r\nTESTS COMPLETED."

    def menu(self):
        """Main Menu loop"""
        box(40, 'c', 'raspiAI', __version__, __url__, '-'*40, __doc__)
        run_menu(40, self.__dict__, 
                ('Text2Speech demo', self._txttospeech),
                ('Twitter [PostTweet-auto] demo', self._twitterauto),
                ('Twitter [PostTweet-prompt] demo', self._twitterprompt),
                ('SpeechRecognition demo', self._speechrecognition),
                ('Vision demo [photo]', self._visionphoto),
                ('Vision demo [video]', self._visionvideo),
                ('Joke demo [random joke]', self._tellrandomjoke),
                ('Joke demo [random joke and Tweet it]', self._tellrandomjokeandtweet),
                ('AIML demo [Pre-set questions]', self._aimldemo))

def start():
    #NOGOOD:    i = demomenu("aiml-en-us-foundation-alice\update1.aiml"), "aiml-en-us-foundation-alice\alice.aiml")
    #           "aiml-en-us-foundation-alice\biography.aiml", "aiml-en-us-foundation-alice\bot.aiml"
    #i = demomenu("aiml-en-us-foundation-alice\default.aiml") #NOT BAD
    i = demomenu("aiml-en-us-foundation-alice\bot.aiml")
    i.menu()

if __name__ == '__main__':
    start()