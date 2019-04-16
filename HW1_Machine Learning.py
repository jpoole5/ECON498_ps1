# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:14:12 2019

@author: Jackson
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

cmc = pd.read_csv("HW1_Parsed_Dataset.csv", header=None)
#Coin Market Cap

# =============================================================================
# 0,market_cap,name,price,supply,symbol,volume
data = cmc.iloc[:2:7]
# target = cmc.iloc[:,1].values
# =============================================================================

data = cmc.iloc[:,1:2]
target = cmc.iloc[:,4:5].values
print(data.head())
print(target)

knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(data, target)

# =============================================================================
# X = 
# 
# print (X)
# 
# results = knn.predict(X)
# 
# print(results)
# =============================================================================
