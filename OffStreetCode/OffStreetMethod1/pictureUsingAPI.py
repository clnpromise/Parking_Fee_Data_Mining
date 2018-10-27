# -*- coding:utf-8 -*-
import requests
import urllib.request
import os
import time


def getAddr(response_dict):	
	for url in response_dict['results']:

		placeid=url['place_id']
		lat=url['geometry']['location']['lat']
		place_url='https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeid+'&fields=url,name,rating,photos&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'
		photos=requests.get(place_url).json()
		result=photos['result']
		if result.__contains__('photos'):
#			print(url['name'])
#			print(url['place_id'])
			for photo_ref in result['photos']:
				photo_url='https://maps.googleapis.com/maps/api/place/photo?maxwidth=5000&photoreference='+photo_ref['photo_reference']+'&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'
				#Change the Download Path!!!
				downloadPath='/Users/chenlingna/Desktop/Project/pictureCrawling/pictures/'+placeid
				if not os.path.exists(downloadPath):
					os.mkdir(downloadPath)
				
				#Save the pictures
				conn = urllib.request.urlopen(photo_url)
				f = open(downloadPath+'/'+photo_ref['photo_reference']+'.jpg', 'wb')
				f.write(conn.read())
				f.close()
				#Store the directions of each picture
				fo.write(downloadPath+'/'+photo_ref['photo_reference']+'.jpg'+'\n')
				
fo=open('paris.txt','w+')
city=input("input the city name: ")
#Calling Place API, change Key if not useful
search_url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=car+park+in+'+city+'&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'

r=requests.get(search_url)
response_dict=r.json()
getAddr(response_dict)

while response_dict.__contains__('next_page_token'):
	time.sleep(2)
	url= search_url+'&pagetoken='+str(response_dict['next_page_token'])
#	print(url)
	r=requests.get(url)
	response_dict.clear()
	#response_dict contains a dictionary of information of each parking lots
	response_dict=r.json()
	#explore each parking lots to download photos
	getAddr(response_dict)

fo.close()
			

	
	
