import numpy as np
import math
import scipy.misc
from timeit import default_timer as timer
import cv2
import numpy as np	
import shutil
import os

def Classify(file):

	img = cv2.imread(file)

	imgInfo = img.shape
	height = imgInfo[0]
	width = imgInfo[1]

	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

	sign_haar = cv2.CascadeClassifier("/Users/chenlingna/Desktop/OnStreetResource/OpenCV Classifier/data/cascade.xml")
	# test the picture, change parameters if needed
	signs = sign_haar.detectMultiScale(img_gray, 1.05, 5, minSize=(44,66))
	n=0
	a=0
	name= file.split('/')
	for sign_x,sign_y,sign_w,sign_h in signs:
		
		[x,y,w,h]= np.int0([sign_x,sign_y,sign_w,sign_h])
		target= img[y:(y+h), x:(x+w)]
#		rect=cv2.rectangle(img, (sign_x, sign_y), (sign_x+sign_w, sign_y+sign_h), (0,255,0), 2)
		
		n+=1
		# change the output direction!!!
		cv2.imwrite('/Users/chenlingna/Desktop/output/'+str(n)+'_'+name[-1], target)
		a=1
	
#	cv2.imshow('img', img)
#	cv2.waitKey(0)


#get the test pictures direction
path='/Users/chenlingna/Desktop/Geelong_Classification/1/'
for line in os.listdir(path):
	if line.endswith('.JPG'):
		Classify(path+line)


