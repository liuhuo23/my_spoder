# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()  # 书名
    price = scrapy.Field()  # 价格
    author = scrapy.Field()  # 作者
    rate = scrapy.Field()  # 评分
    press_year = scrapy.Field()  # 出版年
    comment = scrapy.Field()  # 评论 字典
    press = scrapy.Field()  # 出版社
    translator = scrapy.Field()  # 译者

class MovieItem(scrapy.Item):
    title = scrapy.Field()  #  电影
    img_url= scrapy.Field()  # 封面
    actor = scrapy.Field()  # 演员
    area = scrapy.Field() #  地区
    years = scrapy.Field() # 年代
    plot = scrapy.Field() # 剧情
    type = scrapy.Field() # 类型


