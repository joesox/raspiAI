import os
import sys
from configobj import ConfigObj

__version__ = '0.1.20150419'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI."

class ConfigHelper(object):
    """description of ConfigHelper class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def WriteDemo(self):
        """ Creates a dummy ini file named configfile.ini """
        config = ConfigObj()
        config.filename = "configfile.ini"
        #
        config['keyword1'] = "value1"
        config['keyword2'] = "value2"
        #
        config['section1'] = {}
        config['section1']['keyword3'] = "value3"
        config['section1']['keyword4'] = "value4"
        #
        section2 = {
            'keyword5': "value5",
            'keyword6': "value6",
            'sub-section': {
                'keyword7': "value7"
                }
        }
        config['section2'] = "section2"
        #
        config['section3'] = {}
        config['section3']['keyword 8'] = ["value8", "value9", "value10"]
        config['section3']['keyword 9'] = [11, 12, 13]
        #
        config.write()

    def ReadDemo(self):
        """ 
        Reads the dummy file example.ini
        Must have [faces] section with three faces assigned to face1, face2, face3
        """
        config = ConfigObj("example.ini")
        #
        face1 = config['faces']['face1']
        face2 = config['faces']['face2']
        face3 = config['faces']['face3']
        print "I know: \r\n " + face1 + ", " + face2 + ", & " + face3

    def ReadErrorDemo(self):
        """ 
        Reads the dummy file example.ini
        Tries to readface4which doesn't exist
        """
        try:
            config = ConfigObj("example.ini")
            #
            face4 = config['faces']['face4']
        except LookupError as e:
            print("Could not find key" + str(e))

def demo():
    c = ConfigHelper()
    c.WriteDemo()
    print "Finished WriteDemo demo!"
    print "\r\n"
    c.ReadDemo()
    print "Finished ReadDemo demo!"
    c.ReadErrorDemo()
    print "Finished ReadErrorDemo demo!"
    print "Finished Config demo!"

if __name__ == '__main__':
  demo()



