#!/usr/bin/python3

import  cv2

img=cv2.imread('a.jpg',0)
#  calling  classifier 
casclf=cv2.CascadeClassifier('face.xml')
#  loading  face data 
    face=casclf.detectMultiScale(frame,1.5,5)  #  classifier  tuning parameter
    #print(face)
    for x,y,h,w  in  face:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)  
cv2.waitKey(0) 
cv2.destroyAllWindows()

