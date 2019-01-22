import cv2
import time
import sqlite as sq
import settings

def main():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier("recognizer/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier('recognizer/haarcascade_eye.xml')

    pname = input('Enter User Name : ')
    pid = input('Enter User ID : ')
    sampleNum=0
    try:
        sq.insert_value(pid,pname)
    except:
        pass
    sampleNum=0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            sampleNum += 1
            time.sleep(0.5)
            cv2.imwrite("dataSet/User."+str(pid) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('frame',img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif sampleNum>19:
            break
    cam.release()
    cv2.destroyAllWindows()
    if 'Creation' not in settings.myList:
        settings.myList.append('Creation')

main()