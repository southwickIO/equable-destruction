#!/usr/bin/env python3



###############################################################################
# NAME: evercookie.py		                                                  #
#                                                                             #
# VERSION: 20230223                                                           #
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
#		  2.) ../evercookies.xlsx             	                              #
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
import FindSessionStorage
import SpreadsheetHandler



#defined functions
def main():

	#Run the first check
	chromecookies = FindHTMLCookies.htmlcookiefinder("chrome")
	firefoxcookies = FindHTMLCookies.htmlcookiefinder("firefox")

	#Add the first check to the spreadsheet
	#SpreadsheetHandler.appendSpreadsheet(filepath, "FindHTMLCookies - Chrome", chromecookies)
	#SpreadsheetHandler.appendSpreadsheet(filepath, "FindHTMLCookies - FireFox", firefoxcookies)

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



	#Run the 10th check
	chromesessionstorage = FindSessionStorage.sessioncookiefinder("chrome")
	#firefoxsessionstorage = FindSessionStorage.sessioncookiefinder("firefox")
	edgesessionstorage = FindSessionStorage.sessioncookiefinder("edge")

	#Add the tenth check to the spreadsheet
	SpreadsheetHandler.appendSpreadsheet(filepath, "FindSessionStorage - Chrome", chromesessionstorage)
	#SpreadsheetHandler.appendSpreadsheet(filepath, "FindSessionStorage - FireFox", firefoxsessionstorage)
	SpreadsheetHandler.appendSpreadsheet(filepath, "FindSessionStorage - Edge", edgesessionstorage)

	#stdout
	print("\nSession Storage Finder complete")
	print("Spreadsheet updated\n")


	#Run the 11th check



#entry point
if __name__ == "__main__":
	#set the spreadsheet file path. This must be an absolute filepath
	filepath = "/home/moustache/Desktop/evercookies.xlsx"

	#create the spreadsheet
	workbook = SpreadsheetHandler.createSpreadsheet(filepath)

	main()
else:
	print("This is the main entry point of the application. Please run instead of importing.")
	exit()