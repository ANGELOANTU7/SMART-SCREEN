import numpy as np
import cv2,time,os
import csv,math
import matplotlib.pyplot as plt



def put1 (a,b):
    aa="RAWDATA.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerow([a,b]) 
        csvfile.close()
    print("x:",x," y:",y)
    

            

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
ax=[]
ay=[]
xx=[]
yy=[]
ex=0
ey=0
x=1
y=1
exl=0
eyl=0
xl=0
yl=0
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pic=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            
    xx.append(x)
        
    for hh in range (0,len(xx)):
        yy.append(hh)        


                

    cv2.imshow('frame', frame)
    if ((x-xl)/x)<=1.1 and ((y-yl)/y)<=1.1:
        exl=ex
        eyl=ey
        xl=x
        yl=y 
        put1(x,y)
        
        time.sleep(0.01)
        
        #print("[",ex,",",ey,"],",end =" ")

            



    if cv2.waitKey(1) == ord('q'):
        break

plt.plot(xx,yy) 
plt.show()       

cap.release()
cv2.destroyAllWindows()