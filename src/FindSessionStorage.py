#!/usr/bin/env python3



###############################################################################
# NAME: FindSessionStorage.py                                                 #
#                                                                             #
# VERSION: 20230220                                                           #
#                                                                             #
# SYNOPSIS: Checks for session specific cookies                               #
#                                                                             #
# DESCRIPTION: This script is part of a larger Evercookie checking            #
#              application for Ubuntu machines. This project was created to   #
#              study evercookies.                                             #
#                                                                             #
# INPUT: None.                                                                #
#                                                                             #
# OUTPUT: 1.) STDOUT                                                          #
#                                                                             #
# PRE-RUNTIME NOTES: 1.) This script checks for cookies from default          #
#                        locations.                                           #
#                                                                             #
# AUTHORS: @southwickio                                                       #
#                                                                             #
# LICENSE: GPLv3                                                              #
#                                                                             #
# DISCLAIMER: All work produced by Authors is provided “AS IS”. Authors make  #
#             no warranties, express or implied, and hereby disclaims any and #
#             all warranties, including, but not limited to, any warranty of  #
#             fitness, application, et cetera, for any particular purpose,    #
#             use case, or application of this script.                        #
#                                                                             #
###############################################################################



'''
The following file paths are checked for session storage.

Firefox (decipher with MozLZ4a.py):
    ~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore.jsonlz4
    ~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore-backups/
Chrome (decipher with LDBDump.py):
    ~/.config/google-chrome/Profile 1/Session Storage/
Edge (decipher with LDBDump.py):
    ~/.config/microsoft-edge/Default/Session Storage/
Remember, Edge and Chrome are installed with deb and Firefox is installed with snap.
'''



#import dependencies
import LDBDump
import os


#define functions
def setBrowser(browser):

    #create session directory list
    sessiondirectory = []

    #set cookie path depending on browser
    if browser == 'chrome':
        sessiondirectory.append(os.path.expanduser('~/.config/google-chrome/Profile 1/Session Storage/'))
    elif browser == 'firefox':
        sessiondirectory.append(os.path.expanduser('~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore.jsonlz4'))
        sessiondirectory.append(os.path.expanduser('~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore-backups/'))
    elif browser == 'edge':
        sessiondirectory.append(os.path.expanduser('~/.config/microsoft-edge/Default/Session Storage/'))
    else:
        raise Exception('Invalid browser name')



    return sessiondirectory



def sessioncookiefinder(browser):

    # init variables
    chromesessioncookies = []
    firefoxsessioncookies = []
    iesessioncookies = []

    #set the session directory(s)
    sessiondirs = setBrowser(browser)

    if browser == 'chrome':
        
        #open the associated LDB directory
        db = LDBDump.openLDBDir(sessiondirs[0])

        #read from the associated LDB directory
        LDBDump.getKVPairs(db)

    elif browser == 'firefox':
        pass
    elif browser == 'edge':
        pass
    else:
        raise Exception('Invalid browser name')







#entry point
if __name__ == "__main__":
    print("Please run this application from the main module. Exiting.")
    exit()
else:
    pass