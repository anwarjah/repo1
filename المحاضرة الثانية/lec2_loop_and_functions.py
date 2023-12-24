# -*- coding: utf-8 -*-
"""
Created on Mon Dec 1 11:36:27 2023

@author: حصريا
"""
a=int(input('Enter ineger no.'))
if a%2==0:
    if a>=0:
        print('It  is positive even no.')
    elif a<0:
        print('It  is negative even no.')
else:
       if a>=0:
        print('It  is positive odd no.')
       elif a<0:
        print('It  is negative odd no.')


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for OUTPUT in days:
    print(OUTPUT)
    
# هنا منا بتعريف متغير يحتوي على نص, أي يحتوي على سلسلة من الأحرف
sentence = 'Python is amazing'
for letter in sentence:
    print(letter)

w=range(5)    
d=range(1, 5)
f=range(1,5,2)    
    
for n in range(1, 6):
    print(n)

# بعدها سيتم عرضه .n هنا قمنا بإنشاء سلسلة من الأرقام الموجودة بين 5 إلى 1. في كل دورة في الحلقة سيتم جلب رقم من هذه السلسلة و تخزينه في المتغير
for n in range(5, 0, -1):
    print(n)
    
    
from math import *     # import all defined function 
print(pi)
sqrt(4)
t=2*pi*sqrt(1/9)



sin(90)
cos(30)
tan(90)

4**2
pow(4, 2)        #show help

import pandas as pd 
import numpy as np 
import matplotlib as plt 

 
from PIL import Image, ImageFilter
original=Image.open("Tulips.jpg")
original
print(original.format, original.size, original.mode)
b=original.filter(ImageFilter.BLUR)
b
original
b.save("blur.jpg")

size=(400, 500)
saved="mohammed.jpg"
original=Image.open("Tulips.jpg")
original.thumbnail(size)
original.save(saved)
gray_pict=original.convert('L')
gray_pict.save("gray.jpg")

c=original.filter(ImageFilter.CONTOUR)
c
c.save('contour.jpg')
o=original.filter(ImageFilter.FIND_EDGES())
E=original.filter(ImageFilter.EMBOSS())

m=original.filter(ImageFilter.EDGE_ENHANCE())
m.save('contour.jpg')
n=original.filter(ImageFilter.EDGE_ENHANCE_MORE())
p=original.filter(ImageFilter.SMOOTH())
Q=original.filter(ImageFilter.EMBOSS())

crop=original.crop((0,0,100,100))
crop
crop=original.crop((0,50,100,100))
crop
crop=original.crop((100,50,200,100))
crop


path = 'D:\data_set.csv'
data = pd.read_csv(path ,header=None, names=['Population', 'Profit', 's'])
print(data )
#data=pd.read_csv('E:\dataset\\position_salaries.csv')


path = 'D:\data_set.csv'
data = pd.read_csv(path ,header=None, names=['Population', 'Profit', 's'])
print(data )
#data=pd.read_csv('E:\dataset\\position_salaries.csv')

import speech_recognition 
#####
import nltk
nltk.download()
import speech_recognition as sr

pip install SpeechRecognition
import speech_recognition as sr
        
