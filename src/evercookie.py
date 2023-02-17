#!/usr/bin/env python3



###############################################################################
# NAME: evercookie.py		                                                  #
#                                                                             #
# VERSION: 20230217                                                           #
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
# OUTPUT: 1.) STDOUT														  #
#		  2.) ../evercookies.xlsx"            	                              #
#                                                                             #
# PRE-RUNTIME NOTES: 1.) None.				                                  #
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
import FindHTMLCookies
import FindLocalShareObjects
import FindIsolatedStorage
import SpreadsheetHandler



#defined functions
def main():

	#set the preadsheet file path
	filepath = "../evercookies.xlsx"
	


	#Run the first check
	chromecookies = FindHTMLCookies.htmlcookiefinder("chrome")
	firefoxcookies = FindHTMLCookies.htmlcookiefinder("firefox")

	#Add the first check to the spreadsheet
	SpreadsheetHandler.appendspreadsheet(filepath, chromecookies)
	SpreadsheetHandler.appendspreadsheet(filepath, firefoxcookies)

	#stdout
	print("\nHTML Cookie Finder complete")
	print("Spreadsheet updated\n")



	#Run the second check
	FindLocalShareObjects.lsocookiefinder()
	solfiles = FindLocalShareObjects.searchforsol()

	#stdout
	print("\nLSO Shared Object Finder complete")
	print("Spreadsheet not updated\n")



	#Run the third check
	FindIsolatedStorage.isolatedstoragefinder()

	#stdout
	print("\nIsolated Storage Finder not complete")
	print("Spreadsheet not updated\n")



#entry point
if __name__ == "__main__":
	SpreadsheetHandler.createspreadsheet()
	main()