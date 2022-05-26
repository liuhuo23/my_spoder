import scrapy


class A163Spider(scrapy.Spider):
    name = '163'
    allowed_domains = ['hr.163.com']
    start_urls = ['http://hr.163.com/']

    def parse(self, response):
        trs = response.xpath('//table//tr')
        for tr in trs:
            print(tr.text)
        pass
