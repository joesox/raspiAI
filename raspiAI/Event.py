import os
import sys
import time
from datetime import datetime
from configobj import ConfigObj
from enum import Enum
__version__ = '0.1.20150502'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI."

class EventHow(Enum):
    KEYBOARD = int(0)
    MOUSE = int(1)
    HEARING = int(2)
    VISION = int(3)

class Event(object):
    """
    Holds Event info and static helpers class
    id=-1, name="", whoid=-1, whatid=-1, whenid=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), whyid=-1, howid=-1
    """
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def __init__(self, id=-1, name="", whoid=-1, whatid=-1, whenid=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), whyid=-1, howid=-1):
        """
        Initialize global class variables
        Create Event object
        """
        try:
            self._id = id
            self._name = name
            self._whoid = whoid
            self._whatid = whatid
            self._whenid = str(whenid).strip(None)
            self._whyid = whyid
            self._howid = howid
        except LookupError, x:
            print 'Exception: ', x

    def getList(self):
        """ Returns a string back; eg: 0,LEARNEDNAME,0,0,2015-05-02 12:04:38,0,3 """
        #LIST = self._id, self._name, self._whoid, self._whatid, self._whenid, self._whyid, self._howid
        #return "["+ str(self._id) + "," + self._name + "," + str(self._whoid) + "," + str(self._whatid) + "," + self._whenid + "," + str(self._whyid) + "," + str(self._howid) + "]"
        return str(self._id) + "," + self._name + "," + str(self._whoid) + "," + str(self._whatid) + "," + self._whenid + "," + str(self._whyid) + "," + str(self._howid)

    def RecordEvent(self, configfile=ConfigObj(), sleep=False):
        """
        Send and write all info to their sections; 
        If sleep=True, then sleep a second to generate a new unique timestamp
        NOTE: The [HOW] table stores the last occurance of that specifc HOW value.
                eg:  
        """
        try:
            #[WHO]
            ##ID | EVENTID | 
            LIST = self.getList()
            configfile["WHO"][str(self._whoid)] = LIST
            configfile["WHAT"][str(self._whatid)] = LIST
            configfile["WHEN"][str(self._whenid)] = LIST
            configfile["WHY"][str(self._whyid)] = LIST
            configfile["HOW"][str(self._howid)] = LIST
            configfile.write()
            if (sleep == True):
                time.sleep(1) # Let's sleep a second to generate a new unique timestamp
        except LookupError, x:
            print 'Exception: ', x
        return 0

    def pprint(self):
        """ 
        Pretty Print this Event
        "ID\t| NAME\t\t| WHOID | WHATID | WHENID              | WHYID | HOWID|"
        """
        print("******************")
        print("****  EVENT   ****")
        print("ID\t| NAME\t\t| WHOID | WHATID | WHENID              | WHYID | HOWID|")
        print("-------------------------------------------------------------------------------")
        print(" " + str(self._id) + "\t| " + str(self._name) + "\t|    " + str(self._whoid) + "  |    " + str(self._whatid) + "   | " + str(self._whenid) + " |    " + str(self._whyid)+ "  |    " + str(self._howid) + " |")
        print("**** EVENT END****")

    @staticmethod
    def _GetWhoID_(whoid=-1, configfile=ConfigObj()):
        """ Return full event associated with this WhoID """
        return configfile["WHO"][str(whoid)]

    @staticmethod
    def _GetWhatID_(whatid=-1, configfile=ConfigObj()):
        """ Return full event associated with this WhatID """
        return configfile["WHAT"][str(whatid)]

    @staticmethod
    def _GetWhenID_(whenid=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), configfile=ConfigObj()):
        """ Return full event associated with this WhenID """
        return configfile["WHEN"][whenid]

    @staticmethod
    def _GetWhyID_(whyid=-1, configfile=ConfigObj()):
        """ Return full event associated with this WhyID """
        return configfile["WHY"][str(whyid)]

    @staticmethod
    def _GetHowID_(howid=-1, configfile=ConfigObj()):
        """ Return full event associated with this HowID """
        return configfile["HOW"][str(howid)]

    @staticmethod
    def _GetNextAvailableID_(configfile=ConfigObj()):
        """ Counts all WHEN entries starting at 0 index; Will return next index number available for use """
        try:
            NEXTID = 0      #SECTIONS ARE EMPTY
            #SECTIONS EXISTS
            for subsectionKey in configfile["WHEN"].keys():
                NEXTID = NEXTID + 1
        except:
            NEXTID = 0      #SECTIONS ARE EMPTY
        return NEXTID

def demo():
    #e = Event(0, "LEARNEDNAME", "Joe", "FACEID01", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "GOAL:LEARNFACE", "VISION")
    #Create an Events.ini file to store raspi's knowledge of events
    CONFIG = -1
    fname = "events.ini"
    if(os.path.isfile(fname) == False):
        CONFIG = ConfigObj()
        CONFIG.filename = fname
        CONFIG["WHO"]   = {}
        CONFIG["WHAT"]  = {}
        CONFIG["WHEN"]  = {}
        CONFIG["WHY"]   = {}
        CONFIG["HOW"]   = {}
        CONFIG.write()
    else:
        CONFIG = ConfigObj("events.ini")

    i = Event._GetNextAvailableID_(CONFIG)
    e = Event(i, "LEARNEDNAME", i, i, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i, EventHow.VISION.value)
    e.RecordEvent(CONFIG, True)
    e.pprint()

    i = Event._GetNextAvailableID_(CONFIG)
    e2 = Event(i, "TYPEDTEXT", i, i, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), i, EventHow.KEYBOARD.value)
    e2.RecordEvent(CONFIG, False)
    e2.pprint()

    #SPECIFIC LOOKUPS....
    #print ("Search results for WHOID=1 ...")
    #print (" " + Event._GetWhoID_(1, CONFIG))
    #WHAT = Event._GetWhatID_(1, CONFIG)
    #WHATLIST = WHAT.split(',')
    #print ("Search results for WHATID=1 ...")
    #print (" " + WHAT)
    #WHENID = WHATLIST[4]
    #print ("Search results for WHENID=1 ...")
    #print (" " + Event._GetWhenID_(WHENID, CONFIG))
    #print ("Search results for WHYID=1 ...")
    #print (" " + Event._GetWhyID_(1, CONFIG))
    #HOWID = WHATLIST[6]
    #print ("Search results for HOWID=" + str(HOWID) + " ...")
    #print (" " + Event._GetHowID_(HOWID, CONFIG))

    #RETURN LIST OF ALL LOOKUPS....
    

    print "\r\nFinished Event demo!\r\n"

if __name__ == '__main__':
  demo()

