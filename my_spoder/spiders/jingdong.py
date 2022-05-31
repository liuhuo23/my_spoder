import scrapy
from selenium import webdriver
from my_spoder.MyWebDriver import jingdong_webdriver

class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']
    def __init__(self):
        self.browser = jingdong_webdriver()
        self.start_urls[0] = self.browser.current_url
    def start_requests(self):
        # 把所有的URL地址统一扔给调度器入队列
        url = self.start_urls[0]
        print(url)
        # 交给调度器
        yield scrapy.Request(
            url=url,
            callback=self.parse_html
        )


    def parse_html(self, response):

        pass
