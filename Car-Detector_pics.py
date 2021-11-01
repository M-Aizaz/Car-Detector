# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:36:52 2021

@author: Aizaz
"""

import cv2
import random
car_train = cv2.CascadeClassifier("D:/install/artificial intelligence_install/Anaconda3/Lib/site-packages/cv2/data/cars.xml")

im = cv2.imread("images.jpg")
bw = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
car= car_train.detectMultiScale(bw)
print(car)
#for x,y,w,h in car:
x,y,w,h = car[0] 
cv2.rectangle(im, (x,y),(w+x,h+y),(random.randrange(256),random.randrange(256),random.randrange(256)),2)

cv2.imshow("ss",im)
k=cv2.waitKey(1)
if k==65 or k==97:
   breakpoint()