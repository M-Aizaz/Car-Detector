# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:59:47 2021

@author: Aizaz
"""

import cv2
import random


cap = cv2.VideoCapture(0)

train = cv2.CascadeClassifier("D:/install/artificial intelligence_install/Anaconda3/Lib/site-packages/cv2/data/cars.xml")
while True:
    (check,frame)=cap.read()
    
    if check:
        bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
      break
    codinate=train.detectMultiScale(bw)
    for (x,y,w,h) in codinate:
     cv2.rectangle(frame, (x,y),(w+x,h+y),(random.randrange(256),random.randrange(256),random.randrange(256)),2)
    cv2.imshow('frame',frame)
    ke=cv2.waitKey(1)
    if ke==81 or ke==113:
       break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    