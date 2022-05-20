# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import logging
import pymongo

from itemadapter import ItemAdapter

logger = logging.getLogger(__name__)


class MySpoderPipeline:
    def process_item(self, item, spider):
        return item


class MyDouPipeline:
    def open_spider(self, spider):
        logger.info("开始执行")
        if spider.name == 'douban':
            self.file = open('douban.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'douban':
            # 强转
            item = dict(item)
            # 将字典序列化
            json_data = json.dumps(item, ensure_ascii=False) + ',\n'
            # 将数据写入文件
            self.file.write(json_data)
        return item

    def close_spider(self, spider):
        logger.info("关闭")
        if spider.name == 'douban':
            self.file.close()


class DouMongo:
    conn = None  # mongodb 连接
    mydb = None  # 数据库
    book = None  # 集合

    def open_spider(self, spider):
        logger.error('kaishi')
        self.conn = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.conn['douban']
        self.book = self.mydb['book']
        pass

    def process_item(self, item, spider):
        if spider.name == 'douban':
            item_dict = dict(item)
            self.book.insert_one(item_dict)
        return item

    def close_spider(self, spider):
        pass
