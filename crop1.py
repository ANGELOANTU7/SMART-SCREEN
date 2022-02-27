from inspect import currentframe
from time import time
import cv2 as cv
import numpy as np
import csv,time



crf=0
while True:
    screenh=540
    screenv=360
    img=cv.imread('snip.jpg')
    w,h,_=img.shape
    print("width:",w)
    print("height:",h)

    #cutting

    
    frames=50
    
    with open("CURRENTPOSITION.csv",mode='r') as csvfile :     #readding value from csv
        data=list(csv.reader(csvfile))
        if data is not np.empty:
            currentframe=float(data[0][0])
            cfr=currentframe
        else:
            currentframe=cfr
        
    #currentframe=int(input("enter current frame:"))
    y=h/50
    n=screenh/y
    
    lower=int(0+currentframe*y)
    upper=int((n+currentframe)*y)
    
    
    
    
    
    
    print("upper:",upper)
    print("lower:",lower)
    if upper-lower==screenh and lower<h-screenh:
        croped=img[:screenv,lower:upper]
        cv.imshow('img',croped)
        cv.imwrite('img.jpg',croped)
        
        cv.waitKey(100)

