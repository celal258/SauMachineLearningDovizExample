# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:30:43 2018

@author: celal258
"""
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
#Tarih kismi ay/gun seklinde tabloya cekilmistir. 
dataframe = pd.read_csv('./data.csv')
x=dataframe.iloc[:,0:1].values
y=dataframe.iloc[:,3:4].values

from sklearn.preprocessing import StandardScaler
scaled_x=StandardScaler().fit_transform(x)
scaled_y=StandardScaler().fit_transform(y)

from sklearn.svm import SVR
regressor=SVR(kernel="rbf")
regressor.fit(scaled_x,scaled_y)

plt.scatter(scaled_x,scaled_y,color="red")
plt.plot(scaled_x,regressor.predict(scaled_x),color="blue")
plt.title("Destek Vektör")
plt.xlabel("Tarih")
plt.ylabel("Alis Degeri")
plt.show()