#Used to get the detailed location of parking lot and input it into database;
#This is not used in project since the dataset is too small
# -*- coding:utf-8 -*-
import requests
import urllib.request
import os
import time
import MySQLdb
import re

# connect to the database, change the details!!!
db = MySQLdb.connect("localhost", "root", "", "TestModel", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS location")
# 使用execute方法执行SQL语句
sql = """CREATE TABLE location (
			formatted_address  VARCHAR(100) PRIMARY KEY,
			lat DOUBLE,
			lon DOUBLE,  
			placeID VARCHAR(50))"""

cursor.execute(sql)


def getAddr(response_dict):	
	for url in response_dict['results']:

		placeid=url['place_id']
		lat=url['geometry']['location']['lat']
		lon=url['geometry']['location']['lng']
		address=url['formatted_address'].split(',')[0]
		address=re.sub(r' St',' Street',address)
		address=re.sub(r' Ln',' Lane',address)
		
		print(lat)
		insert = " INSERT INTO location(formatted_address,lat, lon, placeID) VALUES ('%s','%f','%f','%s')" % \
					(address, lat, lon, placeid)
		try:
			# 执行sql语句
			cursor.execute(insert)
			# 提交到数据库执行
			db.commit()
		except:
			# 发生错误时回滚
			db.rollback()
		

#Calling Google Place API to get the location
search_url='https://maps.googleapis.com/maps/api/place/textsearch/json?query=parking+in+Melbourne&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'

r=requests.get(search_url)
response_dict=r.json()
getAddr(response_dict)
while response_dict.__contains__('next_page_token'):
	time.sleep(2)
	url= search_url+'&pagetoken='+str(response_dict['next_page_token'])
	r=requests.get(url)
	response_dict.clear()
	response_dict=r.json()
	getAddr(response_dict)

# close the database
db.close()
			

	
	
