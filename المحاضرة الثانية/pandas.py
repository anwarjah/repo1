# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:24:58 2023

@author: admin
"""

import pandas as pd
'''
ls=["mohammed","ahmed","naji","safe"]


print(ls)
print('\n')
p=pd.Series(ls)
print(p)


ls=["mohammed","ahmed","naji","safi"]
ser=pd.Series(ls,index=['A','B','C','D'])
print(ser)


ls=["mohammed","ahmed","naji","safi"]
ser=pd.Series(ls,index=['A','B','C','D'])
print(ser)
print('\n')

print(ser.values)
print('\n')
print(ser.index)

'''
'''
ls=["mohammed","ahmed","naji","safi"]
ser=pd.DataFrame(ls)
print(ser)
'''
'''
ls=["mohammed","ahmed","naji","safi"]
ser=pd.DataFrame(ls,index=['A','B','C','D'],columns=['Name'])
print(ser.describe())
'''

ls=[1000,2500,4250,7500]
ser=pd.DataFrame(ls,index=['A','B','C','D'],columns=['salary'])
print(ser.describe())
print(ser.agg(['mean','std']))

'''
ls=[10,20,30]
ls1=[100,200,300]
ls2=[1000,2000,3000]
df=pd.DataFrame([ls,ls1,ls2],index=['A','B','C'],columns=['first','second','third'])
print(df.describe())
print(df['first'].describe())
'''

'''
data=pd.read_csv('Feature s4t1m.csv')

print(data)
'''
'''
ls=[10,20,30]
ls1=[100,200,300]
ls2=[1000,2000,3000]
df=pd.DataFrame([ls,ls1,ls2],index=['A','B','C'],columns=['first','second','third'])
df.to_csv('myfile.csv')
'''
'''
data=pd.read_csv('myfile.csv')

print(data)
'''