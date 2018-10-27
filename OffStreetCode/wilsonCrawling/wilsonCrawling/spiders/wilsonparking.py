# -*- coding:utf-8 -*-
import scrapy
from wilsonCrawling.items import WilsoncrawlingItem
import logging
from scrapy.selector import Selector
import re
from lxml import etree
from lxml.html import parse
from urllib2 import urlopen
import os

 
class wilsonparkingSpider(scrapy.spiders.Spider):

	fo= open('crawledURLs.txt','r')
	name = "wilsonparking"
	allowed_domains = ["wilsonparking.com.au"]
	start_urls = []
	urllist=fo.readlines()
	for url in urllist:
		url=re.sub(r'\n','',url)
		start_urls.append(url)
	 
 
	def parse(self, response):
		logging.info("parse: "+ response.url)
		
		search = Selector(response)
		if True:
			rows=[]
			items=search.xpath('//div[@class="CarParkDetailsRates"]//div[@class="CarParkDetailsRatesLabelWrapper"]')
			print(len(items))
			for i in range(1,len(items)):
				logging.info('%d'%i)
				row = WilsoncrawlingItem()
				row['name']=search.xpath('//div[@id="CarParkDetailsAddress"]/address/text()').extract()[0].strip()
				row['lat']=search.xpath('//div[@id="CarParkDetailsAddress"]/address/@data-lat').extract()[0].strip()
				row['lon']=search.xpath('//div[@id="CarParkDetailsAddress"]/address/@data-lon').extract()[0].strip()
				row['scope']=search.xpath('//div[@class="CarParkDetailsRates"]//div[%d]//div[@class="CarParkDetailsRatesLabel"]/text()'%i).extract()[0].strip(),
				row['rate']=search.xpath('//div[@class="CarParkDetailsRates"]//div[%d]//div[@class="CarParkDetailsRatesLabelPrice"]/text()'%i).extract()[0].strip()
				rows.append(row)
				yield row
