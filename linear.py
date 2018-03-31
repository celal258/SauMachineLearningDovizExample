# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 04:12:35 2018

@author: celal258
"""

import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

dataframe = pd.read_csv('./data.csv')
x=dataframe.iloc[:,0:1].values
y=dataframe.iloc[:,3:4].values

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_predictions=regressor.predict(x_test)

plt.scatter(x_train,y_train,color="red")
plt.plot(x_train,regressor.predict(x_train),color="blue")
plt.title("Tarih - Alis")
plt.xlabel("Tarih")
plt.ylabel("Alis Degeri")
plt.show()