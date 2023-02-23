#!/usr/bin/env python3



###############################################################################
# NAME: LDBDump.py                                                            #
#                                                                             #
# VERSION: 20230223                                                           #
#                                                                             #
# SYNOPSIS: LDB File Handler                                                  #
#                                                                             #
# DESCRIPTION: This script is part of a larger Evercookie checking            #
#              application for Ubuntu machines. This project was created to   #
#              study evercookies.                                             #
#                                                                             #
# INPUT: None.                                                                #
#                                                                             #
# OUTPUT: 1.) STDOUT                                                          #
#                                                                             #
# PRE-RUNTIME NOTES: 1.) This script handles LDB directories                  #
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



# import dependencies
import leveldb
import plyvel



#define functions
def openLDBDir(dirpath):

    #opens the directory of the LDB Files
    db = plyvel.DB(dirpath)

    return db



def getKVPairs(db):
    
    cookies = []

    #get the key/value pairs of entries in LDB directory
    for key, value in db:
        cookies.append([key,value])



    return cookies



if __name__ == "__main__":
    print("Please run this application from the main module. Exiting.")
    exit()
else:
    pass