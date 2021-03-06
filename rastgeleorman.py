# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 18:12:04 2018

@author: celal258
"""

import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

#Tarih kismi ay/gun seklinde tabloya cekilmistir. 
dataframe = pd.read_csv('./data.csv')
x=dataframe.iloc[:,0:1].values
y=dataframe.iloc[:,3:4].values
"""
from sklearn.preprocessing import StandardScaler
scaled_x=StandardScaler().fit_transform(x)
scaled_y=StandardScaler().fit_transform(y)
"""
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10)
regressor.fit(x_train,y_train)

y_predictions=regressor.predict(x_test)
