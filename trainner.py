import cv2,os
import numpy as np
from PIL import Image
import sqlite as sq
import settings

def main():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = "dataSet"
    cascadePath = "recognizer/haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascadePath)

    def getImageWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L');
            faceNp = np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow('tainning',faceNp)
            cv2.waitKey(10)
        return IDs,faces

    Ids,faces=getImageWithID(path)
    recognizer.train(faces,np.array(Ids))
    recognizer.write('recognizer/trainningData.yml')
    cv2.destroyAllWindows()
    settings.myList.append('Trainnig')