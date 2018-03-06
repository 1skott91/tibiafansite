# -*- coding: utf-8 -*-
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import time


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TibiaPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '', 'test', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
    
    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO dbcopy (name, vocation, level, exp)
                            VALUES (%s, %s, %s, %s)""", 
                            (item["name"].encode('utf-8'), 
                            item["vocation"].encode('utf-8'),
                            item["level"].encode('utf-8'),
                            item["exp"].encode('utf-8')))
            self.conn.commit()
            
        except MySQLdb.Error:
            e = sys.exc_info()[1]           
        return item
