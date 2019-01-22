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
	except:
		if pname is 'cam_setting':
			settings.myList.append('Camera Settings')
		elif pname is 'face_dataset_creater':
			if 'Creation' not in settings.myList:
				settings.myList.append('Creation')
		else:
			settings.myList.append(pname)
	end = time.clock()
	print("%s Task Completed In : "%(settings.myList[pid]),end='')
	print("%.3gs" %(end-start))