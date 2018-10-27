import cv2
import numpy as np
from pytesseract import pytesseract
import re
import os

def floodfill(x,y,color):
	if x>=len_x: return
	if y>=len_y: return
	if data[x,y]==255:
		data[x,y]=color
		floodfill(x+1, y, color)
		floodfill(x, y+1, color)

def check(img):
	
	out=pytesseract.image_to_string(img,lang='eng',config="-psm 5")
	if out.__contains__('P'):
		return 1

	color=255
	for i in range(len_x):
		for j in range(len_y):
			if data[i,j]==255:
				color-=1
				floodfill(i,j,color)
	print(color)
	for c in range(color,255):
		(a,b)=np.where(data==c)
		if a.shape[0]>0:
			x_min,x_max=np.min(a), np.max(a)
			y_min,y_max=np.min(b), np.max(b)

			if (x_max-x_min>5) and (y_max-y_min>5):
				tmp = data[x_min:x_max, y_min: y_max]
				out=pytesseract.image_to_string(tmp,lang='eng',config="-psm 5")
#				rect=cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0,255,0), 2)
#				#Store the small blocks, change the directions!!!
#				cv2.imwrite('/Users/chenlingna/Desktop/output/'+str(x_min)+'.JPG', tmp)
				if out.__contains__('P') or out.__contains__('F') or out.__contains__('E'):
					return 1
	return 0

root='/Users/chenlingna/Desktop/output/'
with open(root+'output.txt', 'w+') as f:
	for img in os.listdir(root):
		if img.endswith(".JPG"):
			line = root+img+'\n'
			f.write(line)
	
fo = open(root+'output.txt')

for path in fo:
	path=path.strip('\n')
	dsize = 28 #归一化处理的图像大小
	img = cv2.imread(path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	img[img<150]=0
	img[img>=150]=255
	data = np.array(img)
	len_x = data.shape[0] 
	len_y = data.shape[1]
	if check(img)==1:
		name= path.split('/')[-1]
		cv2.imwrite('/Users/chenlingna/Desktop/P_Identification/'+name, cv2.imread(path))
	break
	
fo.close()
	