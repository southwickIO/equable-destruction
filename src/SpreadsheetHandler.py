#!/usr/bin/env python3



###############################################################################
# NAME: spreadsheethandler.py                                                 #
#                                                                             #
# VERSION: 20230220                                                           #
#                                                                             #
# SYNOPSIS: Handles spreadsheet tasks.									      #
#           			                                                      #
#                                                                             #
# DESCRIPTION: This script is part of a larger Evercookie checking            #
#              application for Ubuntu machines. This project was created to   #
#              study evercookies.                                             #
#                                                                             #
# INPUT: None.                                                                #
#                                                                             #
# OUTPUT: 1.) $filepath														  #
#		  2.) stdout			                                              #
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
import openpyxl #pip3 install openpyxl



#stage column headers
headers = ["host_keys", "name", "value", "path", "expires_utc"]



#define functions
def createSpreadsheet(filepath):

	#init workbook/sheet
	workbook = openpyxl.Workbook()
	sheet = workbook.active


	
	#push headers
	for i, header in enumerate(headers):
		sheet.cell(row=1, column=i+1, value=header)



	#save workbook
	workbook.save(filepath)



	return workbook



def stageSpreadsheet(filepath, workbook):
	
	#prep the spreadsheet
	workbook = openpyxl.load_workbook(filepath)
	sheet = workbook.active
	

	return sheet



def addSpace(sheet, maxrow):
	sheet.cell(row=maxrow + 1, column=1, value="")

	return sheet



def addTitle(sheet, maxrow, title):
	sheet.cell(row=maxrow + 1, column=1, value=title)

	return sheet



def appendSpreadsheet(filepath, listofcookies, workbook, title):

	#prep the spreadsheet
	sheet = stageSpreadsheet(filepath, workbook)
	sheet = addSpace(sheet, sheet.max_row)
	sheet = addTitle(sheet, sheet.max_row, title)
	numberofrows = sheet.max_row + 1

	#append the spreadsheet
	for entry in range(len(listofcookies)):
		for i, header in enumerate(headers):

			if title == "FindHTMLCookies":
				sheet.cell(row=numberofrows+entry, column=i+1, value=listofcookies[entry][i])
			elif title == "FindSessionStorage":
				pass
				#do stuff



				#all entries already complete and don't need to be part of the loop
				continue 

	#save workbook
	workbook.save(filepath)



#entry point
if __name__ == "__main__":
	print("Please run this application from the main module. Exiting.")
	exit()
else:
	pass
