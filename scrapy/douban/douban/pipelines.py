# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanPipeline(object):

    #def __init__(self):


    def process_item(self, item, spider):
        try:
            self.connection = pymysql.connect(host='localhost', user='root', password='root', db='douban',
                                              charset='utf8mb4')
            self.cursor = self.connection.cursor()
            sql = 'insert into `movie_top250`(`serial_number`,`movie_name`,`introduce`,`star`,`evaluate`,`describe`) values(%s,%s,%s,%s,%s,%s)'

            self.cursor.execute(sql, (item['serial_number'], item['movie_name'], item['introduce'], item['star'],item['evaluate'], item['describe']))
            self.connection.commit()
        finally:
            self.connection.close()
        return item
