# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files_hw"):
    os.mkdir("html_files_hw")
    #makes html folder
    


for i in range(24):
    current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    print(str(i) + ": " + current_time_stamp)
    f = open("html_files_hw/coinmarketcap.html" + current_time_stamp +".html", "wb")
    response = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/')
    html = response.read()
    print (html)
    f.write(html)
    f.close()
    print ("requesting coin market cap")
    time.sleep(7100)
    
#possible to add a ton of different variations to make website think you are human (won't get banned)