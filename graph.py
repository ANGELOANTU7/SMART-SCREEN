from datetime import datetime
from inspect import currentframe
import numpy as np
import matplotlib.pyplot as plt
import csv,time,os
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
import numpy as np
from scipy.signal import argrelmin, argrelmax
from scipy.interpolate import make_interp_spline
import time as time1
import cv2 as cv
def put1 (a):
    aa="CURRENTPOSITION.csv"
    with open(aa,mode='w',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([a]) 
        csvfile.close()


tim=[]
peakp=[]
down=0


while True:
   
    with open("PDATA.csv",mode='r') as csvfile :     #feeding each values to csv
        data1=list(csv.reader(csvfile))
    #print(data1)
    l=len(data1)
    if l!=0:
        xx=data1[0]
        
    #print(xx)
    with open("VDATA.csv",mode='r') as csvfile :     #feeding each values to csv
        data2=list(csv.reader(csvfile))
    #print(data1)
    l=len(data2)
    if l!=0:
        yy=data2[0]

        
    
    data=xx
    l=len(data)
    x=[] 
    y=[]
    y1=[]
    


    for num in range (0,l):
        x.append(data[num])
        y.append(num)
        y1.append(yy[num])

    x1=np.asarray(x,dtype=np.int32)
  
    y1=np.asarray(y,dtype=np.int32)
    
    z=np.asarray(y1,dtype=np.int32)

    smooth = gaussian_filter1d(x1, 10)
    curve = gaussian_filter1d(smooth, 3)
    smooth1 = gaussian_filter1d(x1, 200)
    
    smooth3=gaussian_filter1d(z,10)

    plt.plot(y1,x1)
    
    
    
    # compute second derivative
    curve_der = np.gradient(np.gradient(curve))
 

    # find switching points
    infls = np.where(np.diff(np.sign(curve_der)))[0]

    rx=float(np.mean(smooth1))
    ry=float(np.mean(smooth3))
    rc=int(smooth[l-1])
    rcy=int(z[l-1])
    
    
    print("current x coordinaties:",rc)
    #print("current y coordinates:",x1[l-2])
    print("reference x point:",rx)
    frames=50 

    p1=5
    p2=5 
    cframe=0
    if(rc>rx):
        print("left")
        print(rc-rx)
        cframe=-(rc-rx)+25
        
    if(rc<rx):
        print("right")
        print(rc-rx)
        cframe=-(rc-rx)+25
    
    nor=[]
    if rc<rx+(p1/100*rx) and rc>rx-(p2/100*rx):
        print("normal")
        cframe=-(rc-rx)+25
        nor.append(-(rc-rx)+25)
        cframe=np.mean(nor)
        
        
        
    if rcy<ry:
        print("UPPPPPPP")
        
    if rcy>ry:
        print("DOWNNN")
        
    print("how many sections should be the image divided into",frames)
    
    if cframe>frames:
        cframe=frames
    if cframe<0:
        cframe=0
    print("current frame:",cframe)
    #put1(cframe)
    
    
    

    
    
    peaks, _ = find_peaks(smooth, height=-60) #points above 0.5
    plt.plot(peaks, smooth[peaks], "x")
    #print(peaks)
    l1=len(peaks)
    if l1>1:
        print(peaks[l1-1])
        print(peaks[l1-2])
    
    ts=0.0
    l3=len(smooth)
    l2=len(peakp)
    if l1>1 and l2>1 :
        peak2=peaks[l1-1]
        
        
    
    
        #if peaks[l1-1]!=peakp[l2-1]:
           # ts = time1.time()
          #  tim.append(ts)
          # peakp=peaks
        
    peakp=peaks
    #print(tim)
    plt.plot(curve)
    plt.plot(smooth1)
    plt.draw()


    
    #plt.plot(smooth_d2 / np.max(smooth_d2), label='Second Derivative (scaled)')
    #for i, infl in enumerate(infls, 1):
     #   plt.axvline(x=infl, color='k', label=f'Inflection Point {i}')
    #plt.legend(bbox_to_anchor=(1.55, 1.0))
    
    
    plt.pause(0.1)
    
    plt.clf()
    np.delete(x1,obj=0)
    np.delete(y1,obj=0)
    os.system('cls')
    
    
    screenh=480
    screenv=360
    img=cv.imread('snip.jpg')
    w,h,_=img.shape
    print("width:",w)
    print("height:",h)

    #cutting

    #x axis
    frames=50
    
    currentframe=cframe
    print("CURRENT FRAME=",currentframe)
    
        
    #currentframe=int(input("enter current frame:"))
    y=h/frames
    n=screenh/y
    
    lower=int(0+currentframe*y)
    upper=int((n+currentframe)*y)
    
    
    
    #y axis
    if currentframe>45 :
        down=down+1
    
    print("DOWN:",down)
        
    vframes=10 
       
    x=w/vframes
    nn=w/10
    if(int(10*down)<w-screenv):
        vlower=int(0+10*down)
    if int(screenv+10*down)<w:
        vupper=int(screenv+10*down)
    
    
    print("upperx:",upper)
    print("lowerx:",lower)
    print("uppery:",vupper)
    print("lowery:",vlower)
    if upper-lower==screenh and lower<h-screenh  :
        croped=img[vlower:vupper,lower:upper]
        cv.imshow('img',croped)
        cv.imwrite('img.jpg',croped)
        

        cv.waitKey(1)
    

    
    
    

    