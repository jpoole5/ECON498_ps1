# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

for i in range(24):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print(str(i) + ": " + current_time_stamp)
	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/')
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(7200)
    
#possible to add a ton of different variations to make website think you are human (won't get banned)