#!/usr/bin/env python3



###############################################################################
# NAME: FindHTMLCookies.py                                                    #
#                                                                             #
# VERSION: 20230216                                                           #
#                                                                             #
# SYNOPSIS: Checks for simple HTML cookies from Chrome and Firefox on an      # 
#           Ubuntu machine                                                    #
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
#                        locations. Google was installed through apt and      #
#                        Firefox was installed through snap. Adjust your      #
#                        filepaths as needed.                                 #
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



#import dependencies
import os
import sqlite3



#define functions
def htmlcookiefinder(browser):

    chromecookies = []
    firefoxcookies = []

    #set cookie path depending on browser
    if browser == 'chrome':
        cookiefile = os.path.expanduser('~/.config/google-chrome/Profile 1/Cookies')
    elif browser == 'firefox':
        cookiefile = os.path.expanduser('~/snap/firefox/common/.mozilla/firefox/qkwknqsj.default/cookies.sqlite')
    else:
        raise Exception('Invalid browser name')

    #connect to database
    conn = sqlite3.connect(cookiefile)
    c = conn.cursor()

    #search database
    if browser == "chrome":
        c.execute('SELECT host_key, name, value, path, expires_utc FROM cookies')
        for row in c.fetchall():
            host_key, name, value, path, expires_utc = row
            chromecookies.append(row)

        return chromecookies

    elif browser == "firefox":
        c.execute('SELECT host, name, value, path, expiry FROM moz_cookies')
        for row in c.fetchall():
            host_key, name, value, path, expires_utc = row
            firefoxcookies.append(row)

        return firefoxcookies


if __name__ == "__main__":
    print("Please run this application from the main module. Exiting.")
    exit()
else:
    pass