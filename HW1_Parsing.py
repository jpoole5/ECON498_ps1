# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:37:58 2019

@author: Jackson
"""

from pandas as pd
from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")
    
pd = pd.dataframe()

for file in glob.glob(html_files/*.html):
    print("parsed " + file)
    f = open(file, "r")
    scrapping_time = os.path.splitext(os.path.basename(file))[0].replace("coinmarketcap","")
    soup = BeautifulSoup(f.read(),'html parser')
    f.close
        #table id = currencies-all
        #then find all tbody
        #then find all tr
        
        
        
        for r in currency_rows:
            
            
        
        