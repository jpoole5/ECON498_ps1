# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:38:31 2019

@author: Jackson
"""


#data = dataset[['currency_change','market_cap','price','supply','volume']].values

#target = dataset[['volume'].values
                 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold
from functools import partial
from operator import is_not
import numpy as np
from sklearn.preprocessing import Normalizer

cmc = pd.read_csv("coinmarketcap_dataset_0422_cleaned.csv")


#Test for volatility correlation with volume

# print(dataset.head())
# =============================================================================
# 
# data = cmc.iloc[:,4:6] 
# #(price and supply)
# 
# #print(data.head())
# 
# target = cmc.iloc[:,2].values
# #(market cap)
# #shows r of .034
# =============================================================================

data = abs(cmc.loc[:,['currency_change']])

#print(data)

target = cmc.loc[:,['volume']].values

#print (target)



     
# =============================================================================
# for val in target: 
#     if val != None : 
#         res.append(val)
# =============================================================================

#def remove_none_elements_from_list(target):
     #return [e for e in target if(pd.notnull(e))]
     
#print(target)

# =============================================================================
# data = cmc.loc[:,['price']]
# target = abs(cmc.loc[:,['currency_change']]).values
# =============================================================================

data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.5,) #random_state = 0)

linear_machine = linear_model.LinearRegression()

linear_machine.fit(data_training,target_training)

prediction = linear_machine.predict(data_test)

print(prediction)

print(metrics.r2_score(target_test,prediction))

plt.scatter(target_test, prediction)
plt.xlabel('target test')
plt.ylabel('prediction')

plt.savefig("scatter_test_prediction.png")

