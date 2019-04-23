# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:37:58 2019

@author: Jackson
"""

import pandas as pd
from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")
    
df = pd.DataFrame()

for file in glob.glob("html_files/*.html"):
    print("parsing " + file)
    f = open(file, "r", encoding="utf-8")
    scrapping_time = os.path.splitext(os.path.basename(file))[0].replace("coinmarketcap","")
    soup = BeautifulSoup(f.read(),'html.parser')
    f.close
    #table id = currencies-all
    #then find all tbody
    #then find all tr
    table = soup.find("table", {"id": "currencies-all"})
    tbody = table.find("tbody")
    currency_rows = tbody.find_all("tr")
    for r in currency_rows:
            symbol = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
            name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
            market_cap = r.find("td", {"class": "market-cap"})['data-sort']
            price = r.find("a",{"class": "price"})['data-usd']
            supply = r.find("td", {"class": "circulating-supply"})['data-sort']
            volume = r.find("a",{"class": "volume"})['data-usd']
            currency_change = r.find("td", {"class": "percent-change"})['data-percentusd']
            df = df.append({
			'symbol': symbol,
			'name': name,
			'market_cap': market_cap,
			'price': price,
			'supply': supply,
            'volume': volume,
            'currency_change': currency_change
			}, ignore_index=True)
    

new_df = df.replace(to_replace=r'None', value= '0', regex=True)

new_df.to_csv("parsed_files/coinmarketcap_dataset_0422_cleaned.csv")


            


            




