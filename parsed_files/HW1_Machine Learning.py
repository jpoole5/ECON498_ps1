# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:14:12 2019

@author: Jackson
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

cmc = pd.read_csv("HW1_Parsed_Dataset.csv", header=None)
#Coin Market Cap

data = cmc.iloc[:2:7]
target = cmc.iloc[:,1].values

#print(data.head())
print(target)

# =============================================================================
# knn = KNeighborsClassifier(n_neighbors=10)
# knn.fit(data, target)
# 
# =============================================================================

