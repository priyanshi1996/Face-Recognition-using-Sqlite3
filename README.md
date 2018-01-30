# Face-Recognition-using-Sqlite3 (Python 3.6)

# Libraries Required 
1. os
2. PIL
3. opencv2
4. sqlite3
5. numpy

This project firstly takes as input User Id and User Name and then creates a dataset of user's face using a webcam. And then that data is fed to a trainer there it is trained by LBPH (Level Binary Pattern Histogram) Classifier and then finally we will be able to recognize faces.

# This Project consists of various files 
1. datasetCreator.py -> creates a dataset
2. trainer.py -> trains the data
3. recognizer.py -> it recognizes the face
4. FaceDataBase.db -> This is the database that store information about faces.(ID, Name)
5. trainingData.ymi -> This is our trained dataset
6. haarcascade_frontalface_default -> This is a default file of opencv used for face detection
7. DataSet -> Its a folder that will contain all the images to be trained. Images are stored in jpeg form


# Instructions to use:-
Download all the files and store them in a folder
And then simply run these three files sequentially
1.datasetCreator.py
2.trainer.py
3.recognizer.py
