import scrapy
from lxml import etree

class GushiSpider(scrapy.Spider):
    name = 'gushi'
    allowed_domains = ['www.gushiwen.cn']
    start_urls = ['http://www.gushiwen.cn/']

    def parse(self, response):
        print("response", response)
        html = etree.HTML(response.text)
        div = html.xpath("//div[@class=\"contson\"]//text()")
        for t in div:
            t = t.replace(' ','')
            print(t)
        pass
