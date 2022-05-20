import logging

import scrapy

from my_spoder.items import BookItem
logger = logging.getLogger(__name__)

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/%E5%90%8D%E8%91%97']

    # 实现换页
    def parse(self, response):
        for i in range(0, 10 * 20, 20):
            url = self.start_urls[0] + "?start=%s&type=T" % i
            yield scrapy.Request(url=url, callback=self.first_page)

    # 获取每一页的书的详细地址
    def first_page(self, response):
        list_a = response.xpath("//ul/li/div[2]")
        logger.info('本页共%s书'%len(list_a))
        for a in list_a:
            item = BookItem()
            item['title'] = a.xpath("./h2/a/@title").extract_first()
            pub = a.xpath('./div[@class="pub"]/text()').extract_first()
            if pub:
                pub = pub.replace("\n","")
                pub = pub.replace(" ","")
            pub_list = pub.split("/")
            item['price'] = pub_list[-1]
            item['press_year'] = pub_list[-2]
            item['press'] = pub_list[-3]
            if len(pub_list)>4:
                item['translator'] = pub_list[-4]
                item['author'] = pub_list[-5]
            else:
                item['translator'] = ""
                item['author'] = pub_list[-4]
            item['rate'] = a.xpath('./div[2]/span[2]/text()').extract_first()
            href = a.xpath("./h2/a/@href").extract_first()
            yield scrapy.Request(url=href+"comments", callback=self.second, meta={"book":item})

    # 进入评论页面
    def second(self, response):
        item = response.meta['book']
        comments = response.xpath('//div[@id="comments"]//ul/li//div[@class="comment"]')
        item['comment']=[]
        for comment in comments:
            person = comment.xpath('./h3/span[2]/a[1]/text()').extract_first()
            time = comment.xpath('./h3/span[2]/a[2]/text()').extract_first()
            content = comment.xpath('./p[@class="comment-content"]/span/text()').extract_first()
            # print(person, time, content)
            conment_one = {'person':person, 'time':time, 'content':content}
            item['comment'].append(conment_one)
            # yield scrapy.Request(url=href, callback=self.third, meta={"book":item})
        logger.info('一本书爬取完毕')
        yield item

    def third(self, response):
        item = response.meta["book"]
        print(item)
        pass
