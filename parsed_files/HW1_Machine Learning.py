# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:14:12 2019

@author: Jackson
"""

import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

cmc = pd.read_csv('test_data.csv')

#cmc = pd.read_csv("coinmarketcap_dataset_0415.csv")
#Coin Market Cap
# =============================================================================

# =============================================================================
# 0,market_cap,name,price,supply,symbol,volume
# =============================================================================

# =============================================================================
# data = cmc.iloc[:,1:2]
# target = cmc.iloc[:,4:5].values
# ============================================================================


data = cmc[['market_cap','volume']]

#target = cmc['price'].values
 
target = pd.factorize(cmc['price'].values)[1].reshape(-1, 1)

data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=.2, random_state=0) 

neigh = KNeighborsRegressor(n_neighbors=2)

neigh.fit(data_train, target_train) 

neigh_predict = neigh.predict([target_test])

print(r2_score(target_test, neigh_predict))





