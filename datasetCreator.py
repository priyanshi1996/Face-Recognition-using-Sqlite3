import cv2
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("FaceDataBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    flag=0
    for row in cursor:
        flag=1
    if(flag==1):
        cmd= "UPDATE People SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People (ID,Name) values ("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=input('Enter user id ')
name=input('Enter user name ')
insertOrUpdate(id,name)

cap=cv2.VideoCapture(0)

sampleNum=0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php
    # for more information about detectMultiscale
    faces=faceDetect.detectMultiScale(gray,1.3,3)
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.rectangle(img,(x,y),(x+h,y+h),(0,255,0),3)
        cv2.imwrite("Dataset/User"+"."+id+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.waitKey(100)
    cv2.imshow('Face',img)
    cv2.waitKey(1)
    if sampleNum>20:
        break

cap.release()
cv2.destroyAllWindows()
    
    