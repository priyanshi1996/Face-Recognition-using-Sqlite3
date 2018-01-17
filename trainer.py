import os
import cv2
from PIL import Image
import numpy as np

#PIL is Python Image Library
#https://www.superdatascience.com/opencv-face-detection/  ..... for more info about LBPH classifier
#Local Binary Pattern Histogram
recognizer = cv2.face.LBPHFaceRecognizer_create()
path='Dataset'
#http://www.pythonforbeginners.com/os/pythons-os-module ....... Details of os library in python

def getImageWithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path) ]
    #print(imagePaths)
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert("L")
        #converted to gray
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        #Dataset\\UserPriyanshi.10.jpg is one imagePath
        #(os.path.split(ImagePath)[-1] is UserPriyanshi.10.jpg where -1 means last portion
        #split('.')[1] is 10 where 1 means middle portion
        faces.append(faceNp)
        print (ID)
        Ids.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(Ids),faces
        
    
Ids,faces=getImageWithId(path)
recognizer.train(faces,Ids)
recognizer.save('trainingData.ymi')
cv2.destroyAllWindows()