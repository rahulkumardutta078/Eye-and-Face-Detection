# Importing Libraries

import cv2

# Loading Cascade

face_cascade=cv2.CascadeClassifier('haar-cascade-files-master\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haar-cascade-files-master\haarcascade_eye.xml')

# Working Function

def detect(gray,frame):
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        rol_gray=gray[y:y+h,x:x+w]
        rol_color=frame[y:y+h,x:x+w]
        
        eyes=eye_cascade.detectMultiScale(rol_gray,1.1,3)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(rol_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    return frame

#        Doing some Face Recognition with the webcam

cap=cv2.VideoCapture(0)
while(True):
    
    #reading webcam frames
    
    ret,frame=cap.read()
    
    # Converting to BGR to gray color
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('video',canvas)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
