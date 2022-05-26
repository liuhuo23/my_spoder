import scrapy
from selenium import webdriver

from my_spoder.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['ziziyy1.com','121.4.190.96:9991']
    start_urls = ['http://ziziyy1.com/mov/0/0/all/4.html']

    def __init__(self):
        self.browser = webdriver.Chrome()
    # 重写start_requests()方法，把所有URL地址都交给调度器
    def start_requests(self):
        # 把所有的URL地址统一扔给调度器入队列
        for offset in range(1,2):
            url = 'http://ziziyy1.com/mov/0/0/all/{}.html'.format(offset)
            print(url)
            # 交给调度器
            yield scrapy.Request(
                url=url,
                callback=self.parse_html
            )

    def parse_html(self, response):
        # 基准的xpath
        dd_list = response.xpath('//ul[@class="main"]/li/a')
        print(len(dd_list))
        # for循环依次遍历
        for dd in dd_list:
            item = MovieItem()
            img_url = dd.xpath('./div[1]/img/@src').extract_first()
            print(img_url)
            title = dd.xpath('./div[2]/p/text()').extract_first()
            print(title)
            item['title'] = title
            item['img_url'] = img_url
            url = dd.xpath('./@href').extract_first()
            yield scrapy.Request(url='http://ziziyy1.com'+url, callback=self.parse_detail, meta={'item':item})
            pass
            # 创建对象'
            # 电影名称
            # 如果不添加extract_first()，会得到一堆列表里面的选择器，但是我们的目标是得到字符串

    def close(spider, reason):
        spider.browser.quit()

    def parse_detail(self, response):
        item = response.meta['item']
        dl = response.xpath('//div[@class="info"]/dl')
        yanyuan = dl.xpath('./dd[1]/text()').extract()
        if (yanyuan is not None) and yanyuan :
            yanyuan = yanyuan[0].split(" ")[1:]
            yanyuan = " ".join(yanyuan)
        item['actor'] = yanyuan
        diqu_niandai = dl.xpath('./dd[2]//text()').extract()
        diqu = ""
        niandai = ""
        if diqu_niandai is not None and diqu_niandai[1] != '年代':
            diqu = diqu_niandai[1]
            niandai = diqu_niandai[3]
        item['area'] = diqu
        item['years'] = niandai
        leixing = dl.xpath('./dd[3]//text()').extract()
        leixing = leixing[2:-2]
        leixing = " ".join(leixing)
        item['type'] = leixing
        juqing = dl.xpath('./dt//div[@class="des2"]/text()').extract()
        item['plot'] = juqing[0]
        print(item)
        pass
