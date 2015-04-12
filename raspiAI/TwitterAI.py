from TwitterAPI import TwitterAPI
__version__ = '0.1.20150412'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI."

class TwitterAI(object):
    """Twitter Class to work with TwitterAPI"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

def demo():
    tweets = TwitterAI()
    print "Finished TwitterAI demo!"

if __name__ == '__main__':
  demo()

