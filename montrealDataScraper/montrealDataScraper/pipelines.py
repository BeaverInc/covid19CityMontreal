# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class MontrealdatascraperPipeline(object):
    def __init__(self):
        self.create_connection()
        # self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect('testingFile_v2.db')
        # self.conn= sqlite3.connect('montrealConfirmedCasesHistory_v2.db')
        self.curr= self.conn.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into DATA values (null,?,?,?,?)""",(
            item['boroughName'],
            item['confirmedCase'],
            item['date'],
            item['time']
        ))
        self.conn.commit()