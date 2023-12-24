# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:00:20 2023

@author: User
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sb
import matplotlib.pyplot as plt

data=pd.read_csv("fraud_detection_bank_dataset.csv")
print(data)
x=data.iloc[:,:-1]
y=data.iloc[:,110]


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print(model.score(x_test,y_test))

print(accuracy_score(y_test,y_pred))


colors=np.where(y_test==1,'blue','green')

plt.scatter(x_test.iloc[:,0], y_test, c=colors,label="Actual Data" ,marker=("o"))
plt.xlabel("Targets")
plt.ylabel('Information')
plt.title("Tech victms")
plt.show()

plt.scatter(x_test.iloc[:,0], y_pred, c=colors,label="Predected Data" ,marker=("x"))
plt.xlabel("Targets")
plt.ylabel('Information')
plt.title("Tech victms pred")

plt.pie([np.sum(y_test==0),np.sum(y_test==1)],labels=['class0','class1'],colors=['blue','red'],autopct='%1.1f%%')


plt.pie([np.sum(y_pred==0),np.sum(y_pred==1)],labels=['class0','class1'],colors=['blue','red'],autopct='%1.1f%%')
plt.title('Pie Info')



plt.bar(['class0','class1'],[np.sum(y_pred==0),np.sum(y_pred==1)],color=colors)


cm=confusion_matrix(y_test,y_pred)

sb.heatmap(cm,annot=True,fmt="d",cmap="Blues",xticklabels=['class0','class1'],yticklabels=['class0','class1'])
plt.show()








