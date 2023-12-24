# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:08:12 2023

@author: User
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl


data=pd.read_csv('economic_data.csv')
print(data)

print(data.describe())
print(data.head())


x=data.iloc[:,:1]
y=data.iloc[:,1]

print(x)
print(y)

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)

mpl.scatter(x, y)
mpl.plot(x,model.predict(x),'r')