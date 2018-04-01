"""
Created on Sat Mar 31 13:07:39 2018

@author: celal258
"""

import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
#Tarih kismi ay/gun seklinde tabloya cekilmistir. 
dataframe = pd.read_csv('./data.csv')
x=dataframe.iloc[:,0:1].values
y=dataframe.iloc[:,3:4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_regressor=PolynomialFeatures(degree=4)
x_poly=poly_regressor.fit_transform(x)
x_test_poly=poly_regressor.fit_transform(x_test)
poly_regressor.fit(x_poly,y)
regressor=LinearRegression()
regressor.fit(x_poly,y)
y_predictions=regressor.predict(x_test_poly)

plt.scatter(x,y,color="red")
plt.plot(x,regressor.predict(x_poly),color="blue")
plt.title("Polinom")
plt.xlabel("Tarih")
plt.ylabel("Alis Degeri")
plt.show()