# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:41:06 2019

@author: Jackson
"""

import pandas as pd
from bs4 import BeautifulSoup
import os
import glob

df = pd.read_csv("coinmarketcap_dataset_0422.csv")
df = df.replace('"None"', df.replace(['"None"'], ['"0"'])

df.to_csv("parsed_files/coinmarketcap_dataset_0422.csv")




