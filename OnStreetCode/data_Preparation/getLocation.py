import requests
import urllib.request
import os
import time


def getAddr(response_dict):	
	i=0
	street=0
	for url in response_dict['results']:
		street+=1

		viewpoint=url['geometry']['viewport']
		minlat=int(round(viewpoint['southwest']['lat'],4)*10000)
		maxlat=int(round(viewpoint['northeast']['lat'],4)*10000)
		minlon=int(round(viewpoint['southwest']['lng'],4)*10000)
		maxlon=int(round(viewpoint['northeast']['lng'],4)*10000)
		for lat in range(minlat,maxlat, 5):
			for lon in range(minlon,maxlon, 5):
				for heading in range(0,360,30):
					i+=1
					output.write(str(lat/10000)+'_'+str(lon/10000)+'_'+str(heading)+'_-0000.JPG'+'\n')
	print(i)
	return street
		
city = input("Input your city name: ")
output= open(city+'_Street_Locations','w+')

#change key!!!
search_url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=street+in+'+city+'+City+Australia&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'

#calling API
n=0
r=requests.get(search_url)
response_dict=r.json()
n=n+getAddr(response_dict)

while response_dict.__contains__('next_page_token'):
	time.sleep(2)
	url= search_url+'&pagetoken='+str(response_dict['next_page_token'])
	print(url)
	r=requests.get(url)
	response_dict.clear()
	response_dict=r.json()
	n=n+getAddr(response_dict)
print(n)

output.close()