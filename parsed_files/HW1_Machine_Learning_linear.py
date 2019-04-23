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

cmc = pd.read_csv("coinmarketcap_dataset_0422_cleaned.csv")


#Test for volatility correlation with volume


data = cmc.loc[:,['volume']]

#print(data)

target = abs(cmc.loc[:,['currency_change']]).values

#print (target)

#fitting the data 
data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.25, random_state = 0)

linear_machine = linear_model.LinearRegression()

linear_machine.fit(data_training,target_training)

prediction = linear_machine.predict(data_test)

print(prediction)

print(metrics.r2_score(target_test,prediction))

plt.scatter(target_test, prediction)
plt.xlabel('target test')
plt.ylabel('prediction')

plt.savefig("HW_Scatterplot")

