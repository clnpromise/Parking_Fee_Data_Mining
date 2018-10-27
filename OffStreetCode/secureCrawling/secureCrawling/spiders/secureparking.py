#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
from secureCrawling.items import SecurecrawlingItem
import logging
from scrapy.selector import Selector
import re
from lxml import etree
from lxml.html import parse
from urllib2 import urlopen

 
class secureparkingSpider(scrapy.spiders.Spider):
	name = "secureparking"
	allowed_domains = ["secureparking.com.au"]
	
	fo= open('crawledURLs.txt','r')
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
			items=search.xpath('//table[@class="ui selectable table"]/tbody[1]//tr')
			print(items)
			for i in range(1,len(items)):
				logging.info('%d'%i)
				row = SecurecrawlingItem()
				row['name']=search.xpath('//div[@class="map-list-content"]/h1/text()').extract()[0].strip()
				row['address']=search.xpath('//div[@class="map-list-content"]/p/strong/text()').extract()[0].strip()
				row['scope']=search.xpath('//table[@class="ui selectable table"]/tbody[1]//tr[%d]//label/text()'%i).extract()[0].strip()
				row['rate']=search.xpath('//table[@class="ui selectable table"]/tbody[1]//tr[%d]//span/div[1]/text()'%i).extract()[0].strip()
				rows.append(row)
				yield row

				
