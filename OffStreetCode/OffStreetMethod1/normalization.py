#!/usr/bin/python
import re
import requests
import urllib.request

filein= open ('pictureToWords.txt','r')
fileout= open ('pictureDB.txt','w')
hours= re.compile(r'(\d{1,2}(\.\d{1,2})?)((\-\d{1,2}(\.\d{1,2})?)|\+)[HhRrSsou]{1,5}')
name=''
while True:
	word=filein.readline().replace(" ","")
	word=word.replace("\n","")
	if not word:
		break
	if re.match(r'NewParkingLotBeginsHere', word):
		path=filein.readline()
		place_url='https://maps.googleapis.com/maps/api/place/details/json?placeid='+path.split('/')[0]+'&fields=url,name,formatted_address&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'

		result=requests.get(place_url).json()

		name=result['result']['formatted_address']
		print(name)
		fileout.write(path+'\n')
	if re.match(hours, word):
		if re.search(r':',word):
			print(word)
			word=re.sub(r'[HhRrSsou]{1,5}', r'', word)
			print(word)
			word=re.sub(r':[s$]?',r'Hrs $',word)
			print(word)
			fileout.write(name+' '+word+'\n')
		else:
			fileout.write(name+' '+re.sub(r'[HhRrSsou]{1,5}', r'', word)+'Hrs '+'$'+re.sub(r'[s$]?','',filein.readline()))
filein.close()
fileout.close()
		
	