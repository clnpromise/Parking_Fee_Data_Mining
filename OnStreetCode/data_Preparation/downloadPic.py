# Download Pictures from Street View according to location
# _*_ coding: utf-8 _*_
 
import urllib
#import urllib2
import urllib.request
import requests
import threading
from optparse import OptionParser
from bs4 import BeautifulSoup
import sys
import re
import os
import random
import hashlib
import time
from urllib.request import urlretrieve
import shutil

proxy_list = []


headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}


def download(url, name):
	time.sleep(2)
 
	try:
		response = urllib.request.Request(url,headers=headers)
		conn = urllib.request.urlopen(response)

		f = open(name, 'wb')
		f.write(conn.read())
		f.close()
		print('Pic Saved!')
	except urllib.request.HTTPError:
		print('Error')
		


fp = open('download15.0.txt', "r+")
path=os.getcwd()
os.mkdir(path+'/pictures/')

for line in fp.readlines():
	zu = line.split('_')
	lat = zu[0]
	lng = zu[1]
	heading = zu[2]

	name = path+"/pictures/" + lat + "_" + lng + "_25_"+heading + "_"+ zu[3].replace('\n','')
	

	metaUrl="https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location="+lat+","+lng+"&heading="+heading+"&pitch=-004&key=AIzaSyD-KBrHljAyyC5rtPEUC3e7j6E9e7VOKGY"
	metaResult=requests.get(metaUrl).json()
	status=metaResult['status']

	if status=="OK":
		lat=metaResult['location']['lat']
		lng=metaResult['location']['lng']
		pano = metaResult['pano_id']
		url = "https://maps.googleapis.com/maps/api/streetview?size=640x640&location="+str(lat)+","+str(lng)+"&heading=" +heading + "&fov=25&pitch=-004&key=AIzaSyD-KBrHljAyyC5rtPEUC3e7j6E9e7VOKGY"
		print(name)
		print(url)
		download(url, name)
fp.close()

