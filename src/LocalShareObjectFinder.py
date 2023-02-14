#!/usr/bin/env python3



###############################################################################
# NAME: LocalShareObjectFinder.py                                             #
#                                                                             #
# VERSION: 20230213                                                           #
#                                                                             #
# SYNOPSIS: Main script that runs the other scripts.					      #
#           			                                                      #
#                                                                             #
# DESCRIPTION: This script is part of a larger Evercookie checking            #
#              application for Ubuntu machines. This project was created to   #
#              study evercookies.                                             #
#                                                                             #
# INPUT: None.                                                                #
#                                                                             #
# OUTPUT: 1.) STDOUT                                                          #
#                                                                             #
# PRE-RUNTIME NOTES: 1.) I would have ran the find command using the          #
#                        subprocess library, however I couldn't find a way to #
#                        run a sudo command to wait for password input        #
#                        without messing with visudo. I learned that it is    #
#                        not possible to display a password prompt when       #
#                        running a sudo command via subprocess in Python and  #
#                        have the user enter the password because the         #
#                        subprocess module runs the command in a separate     #
#                        process.			                                  #
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
From wikipedia:

A local shared object (LSO), commonly called a Flash cookie (due to its 
similarity with an HTTP cookie), is a piece of data that websites that use 
Adobe Flash may store on a user's computer. Local shared objects have been used
by all versions of Flash Player (developed by Macromedia, which was later 
acquired by Adobe Systems) since version 6.

Flash cookies, which can be stored or retrieved whenever a user accesses a page
containing a Flash application, are a form of local storage. Similar to 
cookies, they can be used to store user preferences, save data from Flash 
games, or track users' Internet activity. LSOs have been criticised as a breach
of browser security, but there are now browser settings and addons to limit the
duration of their storage.

Adobe Flash Player does not allow third-party local shared objects to be shared
across domains. For example, a local shared object from "www.example.com" 
cannot be read by the domain "www.example.net". However, the first-party
website can always pass data to a third-party via some settings found in the
dedicated XML file and passing the data in the request to the third party.
Also, third-party LSOs are allowed to store data by default. By default, LSO
data is shared across browsers on the same machine.
'''


#import dependencies
import os
import re
import fnmatch



#define functions
def lsocookiefinder():

	#set the directory and check if it exists
	flashcookiedir = os.path.expanduser("~/.macromedia/Flash_Player/")

	if os.path.exists(flashcookiedir):

		print("\n\n\n\n\n\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~ THE LSO DIRECTORY EXISTS ~~~~~~~~~~~~~~~~~~~~\n\n\n\n\n\n\n\n\n\n")



		#go through the files in the directory and search for any .sol files
		for root, dirs, files in os.walk(flashcookiedir):

			for file in files:

				if re.match(r".*\.sol", file):

					print('\n', os.path.join(root, file), '\n')
	else:
		print("\nLSO directory does not exist. Checking for .sol files\n")



def searchforsol(filename="*.sol", rootdir='/'):

	#initialize variables
	matchingfiles = []


	#search for .sol files
	for root, dirs, files in os.walk(rootdir):

		for f in files:

			if fnmatch.fnmatch(f, filename):

				matchingfiles.append(os.path.join(root, f))


	#stdout
	if not matchingfiles:

		print("\nNo .sol files located\n")



	return matchingfiles