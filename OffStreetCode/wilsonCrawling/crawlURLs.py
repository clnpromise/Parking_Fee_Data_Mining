#!/usr/bin/python
from selenium import webdriver
import time
import os

path=os.getcwd()

fo= open(path+'/crawledURLs.txt','w+')

#use selenium to crawl
browser = webdriver.Chrome()
#ensure the window size is big enough 
browser.set_window_size(1000,30000)
#change the url if you want to crawl car parks in another place
browser.get("https://www.wilsonparking.com.au/find-a-park/VIC/Melbourne%20CBD")
#ensure enough time to crab the data 
time.sleep(5)

elements=browser.find_elements_by_xpath('//a[@href]')

for element in elements:
	url = element.get_attribute("href")
	#get the target URLs
	if url.startswith('https://www.wilsonparking.com.au/park/'):
		#transform the URL so that we can crawl the data needed
		new=url.replace("https://www.wilsonparking.com.au/park/","")
		values = new.split('_')
		header="https://www.wilsonparking.com.au/_layouts/15/WilsonParking.ashx?method=GetCarParkDetails"
		stationNo="&args%5BstationNumber%5D="+values[0]
		carparkName="&args%5BcarparkName%5D="+values[1]
		fo.write(header+stationNo+carparkName+'\n')

browser.close() 
fo.close()


