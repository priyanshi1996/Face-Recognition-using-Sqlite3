import cv2
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainingData.ymi')

cap=cv2.VideoCapture(0)

id=0

def getProfile(id):
    conn=sqlite3.connect("FaceDataBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+h,y+h),(0,255,0),3)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        
        profile=getProfile(str(id))
        if(profile!=None):
            cv2.putText(img,str(profile[0]),(x,y+h+30),font,1,(0,0,255),2,cv2.LINE_AA)
            cv2.putText(img,str(profile[1]),(x,y+h+60),font,1,(0,0,255),2,cv2.LINE_AA)
        else:
            cv2.putText(img,str(id),(x,y+h+30),font,1,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
    
    