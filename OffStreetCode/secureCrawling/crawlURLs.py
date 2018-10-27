#!/usr/bin/python
from selenium import webdriver
import time

fo= open('crawledURLs.txt','w+')

#use selenium to crawl
browser = webdriver.Chrome()
#ensure the window size is big enough 
browser.set_window_size(1000,30000)
browser.get("https://www.secureparking.com.au/en-au/car-parks#lat=-37.81361100000001&long=144.96305600000005&Add=Melbourne%20VIC,%20Australia&Sort=+Distance&sp=0&ProductTypes=undefined&Entry=undefined&Exit=undefined&D=undefined&A=undefined&P=undefined&R=undefined&T=undefined")
#ensure enough time to crab the data 
time.sleep(5)

elements=browser.find_elements_by_xpath('//label[@data-url]')

for element in elements:
	url = element.get_attribute("data-url")
	#get the target URLs
	if url.startswith('https://www.secureparking.com.au/en-au/car-parks/'):
		#transform the URL so that we can crawl the data needed
		fo.write(url+'\n')

browser.close() 
fo.close()


