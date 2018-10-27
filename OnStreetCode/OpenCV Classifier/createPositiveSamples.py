import os
#change the direction!!!
dire="/Users/chenlingna/Desktop/Classifier"
# all pictures to be sampled should be stored in sample file 
sample= dire+"/sample"
for img in os.listdir(sample):
	if img.endswith(".JPG") or img.endswith(".jpeg"):
		name=str(img).split('.')[0]
		os.chdir(dire)
		os.mkdir(name)
		os.system("opencv_createsamples -img sample/"+img+" -bg neg.txt -info "+name+"/"+name+".txt -maxxangle 0 -maxyangle 1.3 -maxzangle 0 -num 100 -maxidev 20 -w 20 -h 30 -bgthresh 0")


file_data=""
n=0
for img in os.listdir(sample):
	if img.endswith(".JPG") or img.endswith(".jpeg"):
		path=str(img).split('.')[0]
		os.chdir(dire)

		fo = open (path+"/"+path+".txt",'r')
		for line in fo:
			file_data += path+'/'+line
			n+=1
		print(path)
		print(n)
		fo.close()

	
fo = open ("pos.txt",'w+')
fo.write(file_data)
fo.close()

fo = open('pos.txt','r')
n=0
a=[]
for line in fo:
	a.append(line)
	n+=1

s= n // 100
fo.close()

filedata=''
for j in range (0,100):
	for i in range(0,s):
		filedata+=a[100*i+j]
fo=open('pos.txt','w')
fo.write(filedata)
fo.close()

os.system("opencv_createsamples -info pos.txt -num "+str(n)+" -w 20 -h 30 -vec pos.vec")