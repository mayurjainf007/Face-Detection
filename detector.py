import cv2
import numpy as np
import sqlite as sq
import settings

def main():
    recog = cv2.face.LBPHFaceRecognizer_create()
    # recog.read('recognizer/trainning.yml')
    recog.read('recognizer/trainningData.yml')
    cascadePath = "recognizer/haarcascade_frontalface_default.xml"
    faceDetect = cv2.CascadeClassifier(cascadePath)

    cam = cv2.VideoCapture(0)
    name = ''
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img =cam.read()
        gray=   cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray, 1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            ids, conf = recog.predict(gray[y:y+h,x:x+w])
            name = sq.select_task_name(ids)
            cv2.putText(img,str(name),(x,y+h),font,0.55,(0,255,0),1)
        cv2.imshow('Face',img) 
        if cv2.waitKey(1)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    settings.myList.append('Detection')