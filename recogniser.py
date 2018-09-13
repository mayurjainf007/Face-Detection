import cv2,os
import numpy as np
from PIL import Image
import settings

def main():
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	path = "dataSet"
	cascadePath = "recognizer/lbpcascade_frontalface.xml"
	detectors = cv2.CascadeClassifier(cascadePath)

	def getImagesAndLabels(path):
		imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
		faceSamples=[]
		Ids=[]
		for imagePath in imagePaths:
				pilImage=Image.open(imagePath).convert('L')
				imageNp=np.array(pilImage,'uint8')
				Id=int(os.path.split(imagePath)[-1].split(".")[1])
				faces=detectors.detectMultiScale(imageNp, scaleFactor=1.2, minNeighbors=5)
				for (x,y,w,h) in faces:
					faceSamples.append(imageNp[y:y+h,x:x+w])
					Ids.append(Id)
		return faceSamples,Ids

	faces,Ids = getImagesAndLabels('dataSet')
	recognizer.train(faces, np.array(Ids))
	recognizer.write('recognizer/trainning.yml')
	cv2.destroyAllWindows()
	settings.myList.append('Recognization')