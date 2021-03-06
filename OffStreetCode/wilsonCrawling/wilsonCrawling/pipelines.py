# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import MySQLdb.cursors
class WilsoncrawlingPipeline(object):
        #数据库参数
        def __init__(self):
                dbargs = dict(
                         host = '115.146.85.189', #
                         db = 'MelParking', #
                         user = 'root', #root
                         passwd = '31415926', #31415926
                         cursorclass = MySQLdb.cursors.DictCursor,
                         charset = 'utf8',
                         use_unicode = True,
                         port='3306'
                        )
                self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

        '''
        The default pipeline invoke function
        '''
        def process_item(self, item,spider):
                res = self.dbpool.runInteraction(self.insert_into_table,item)
                return item
        #插入的表，此表需要事先建好
        def insert_into_table(self,conn,item):
                        conn.execute('insert into wilsonParking(name,lat,lon,scope,rate) values(%s,%s,%s,%s,%s)',            
                                (
                                item['name'],
                                item['lat'],
                                item['lon'],
                                item['scope'],
                                item['rate']
                                ))