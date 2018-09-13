import time
import face_dataset_creater
import trainner
import recogniser
import detector
import settings

def main(pid,pname):
	try:
		start = time.clock()
		module = __import__(pname)
		func = getattr(module, 'main')
		func()
		end = time.clock()
		print("%s Task Completed In : "%(settings.myList[pid]),end='')
		print("%.3gs" %(end-start))
	except:
		settings.myList.append('Untitled')