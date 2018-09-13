from tqdm import trange
import time, count, settings

def main():
	settings.init()
	print ("Starting Face Detection Technique")
	for i in trange(0,10):
		time.sleep(0.01)
	print(" If Data Already Feeded.(Press Ctrl Z)")
	count.main(0,'face_dataset_creater')
	count.main(1,'trainner')
	count.main(2,'recogniser')
	count.main(3,'detector')
	print ("Completed")

if __name__ == '__main__':
	main()