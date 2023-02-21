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

Firefox:
    /home/moustache/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore.jsonlz4
    /home/moustache/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/sessionstore-backups/
Chrome:
IE:
Remember IE and Chrome are installed with deb and Firefox is installed with snap.
'''
#import dependencies
import LDBDump


#define functions
def setBrowser():
    return sessionfile



def sessioncookiefinder(browser):

    chromesessioncookies = []
    firefoxsessioncookies = []
    iesessioncookies = []

    #set cookie path depending on browser
    if browser == 'chrome':
        sessiondirectory = os.path.expanduser('~/.config/google-chrome/Profile 1/Session Storage/')
    elif browser == 'firefox':
        sessiondirectory = os.path.expanduser('~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/cookies.sqlite')
    elif browser == 'ie':
        sessiondirectory = os.path.expanduser('~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/cookies.sqlite')
    else:
        raise Exception('Invalid browser name')

'''
firefox session store in 2 areas
sessionstore-backups/
sessionstore.jsonlz4
'''

#entry point
if __name__ == "__main__":
    print("Please run this application from the main module. Exiting.")
    exit()
else:
    pass