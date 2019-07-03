#!/usr/bin/python3

import  cv2
#  calling  classifier 
casclf=cv2.CascadeClassifier('face.xml')
casclf1=cv2.CascadeClassifier('eye.xml')
#  loading  face data 
cap=cv2.VideoCapture(0)

while cap.isOpened() :
    status,frame=cap.read()
    #  now we can apply  classifier in  live frame 
    face=casclf.detectMultiScale(frame,1.5,5)  #  classifier  tuning parameter
    #print(face)
    for x,y,w,h  in  face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)  
        #  only  face
        facedata=frame[y:y+h,x:x+w]   
        #cv2.imshow('f',facedata)
        eye=casclf1.detectMultiScale(facedata)
        for ex,ey,ew,eh  in  eye:
            cv2.rectangle(facedata,(ex,ey),(ex+eh,ey+ew),(0,0,255),2)
    cv2.imshow('face',frame)  
    if  cv2.waitKey(10)  &  0xff  == ord('q') :
        break

cv2.destroyAllWindows()
cap.release()

