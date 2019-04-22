# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:38:31 2019

@author: Jackson
"""


#data = dataset[['market_cap','price','supply','volume']].values

#target = dataset[['volume'].values
                 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold

cmc = pd.read_csv("coinmarketcap_dataset_0422.csv")


#Test for volatility correlation with volume

# print(dataset.head())

data = cmc.iloc[:,7]

print(data.head())

target = cmc.iloc[:,1].values

print(target)


