from tqdm import trange
import time, settings, count

def main():
	settings.init()
	flag = True
	count.main(0,'detector')
	print ("Starting Face Detection Technique")
	for i in trange(0,10):
		time.sleep(0.01)
	print(" If Data Already Feeded.(Press Ctrl Z)")
	while(flag):
		count.main(1,'face_dataset_creater')
		try:
			print("Press Enter To Skip To Recognition Part or Any Key To Feed New Data :")
			flag = input()
		except:
			flag = False
	count.main(2,'trainner')
	count.main(3,'recogniser')
	count.main(4,'detector')
	print ("Completed")
	print(settings.myList)

if __name__ == '__main__':
	main()