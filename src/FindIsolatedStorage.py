#!/usr/bin/env python3



###############################################################################
# NAME: FindIsolatedStorage.py                                                #
#                                                                             #
# VERSION: 20230217                                                           #
#                                                                             #
# SYNOPSIS: Checks for Isolated Storage artifacts from Microsoft Silverlight  #                                                   #
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
Isolated Storage is a Microsoft Silverlight storing mechanism. This storage 
mechanism is called Isolated Storage because the store is partitioned, and a 
Silverlight application has access only to certain parts.

You cannot access any old stored data. The store is partitioned per user.
'''



'''
After searching my file system and Microsoft documentation, I
Isolated storage is a Microsft feature not specifically tied to Silverlight, 
although that is what it was known for. Isolated Storage is available for 
devleopers who develop extension/apps for Edge and Windows so I am still a bit 
suspicious that I didn't find anything even though I know Silverlight is defunct.

This script is not developed because no evidence of Isolated Storage for 
Microsoft Edge on Ubuntu 22.04 was found.
'''



#define functions
def isolatedstoragefinder():
	pass



#entry point
if __name__ == "__main__":
    print("Please run this application from the main module. Exiting.")
    exit()
else:
    pass