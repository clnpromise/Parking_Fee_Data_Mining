# -*- coding:utf-8 -*-
import MySQLdb
import re
import requests
import urllib.request

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TestModel", charset='utf8' )
cursor = db.cursor()
sql = """CREATE TABLE secureLocation (
			name  VARCHAR(100) PRIMARY KEY,
			lat DOUBLE,
			lon DOUBLE,  
			placeID VARCHAR(50))"""

cursor.execute(sql)


sql = """SELECT DISTINCT name, address FROM secureParking"""

# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
for row in results:
	address = row[1]
	name = row[0]
	print('name: '+name+'; address: '+address)
	
	search_url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='+address+'&key=AIzaSyAW7BA78s2aJn1-Dybjv9PVIIMghJQWLU4'
	r=requests.get(search_url)
	response_dict=r.json()
	lat=response_dict['results'][0]['geometry']['location']['lat']
	lon=response_dict['results'][0]['geometry']['location']['lng']
	placeid=response_dict['results'][0]['place_id']
	print(response_dict['results'][0]['formatted_address']+' '+str(lat)+' '+str(lon))
	
	insert = " INSERT INTO secureLocation(name, lat, lon, placeID) VALUES ('%s','%f','%f','%s')" % \
			(name, lat, lon, placeid)
	try:
		# 执行sql语句
		cursor.execute(insert)
		# 提交到数据库执行
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()



# 关闭数据库连接
db.close()


