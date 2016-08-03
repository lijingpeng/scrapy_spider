# -*- coding: UTF-8 -*-
import scrapy
from scrapy_spider.items import SpiderItem
from scrapy_spider.parse_url import parse

class qq_search_spider(scrapy.Spider):
    name = "qq_search_spider"
    allowed_domains = ["news.sogou.com"]

    def __init__(self):
        self.count = 0

    def start_requests(self):
        base_url = "http://news.sogou.com/news?mode=1&manual=true&query=site:qq.com+'零售'&sort=0&page=%s&dp=1"
        for i in range(1, 10, 1):
            url = base_url % i
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        for section in response.xpath('//div[@class="vrwrap"]'):
            info = section.xpath('.//a')[0]
            link = info.xpath('@href').extract()[0].encode('utf-8')
            title = "".join(info.xpath('text()').extract()).encode('utf-8')
            author = "".join(section.xpath('.//p/text()').extract()).encode('utf-8')
            print '------------now parse url:', link
            result = parse(link)
            if result is None or result['content'] == '':
                continue

            item = SpiderItem()
            item['title'] = title
            item['link'] = link
            item['author'] = result['author']
            item['createTime'] = result['createTime']
            item['remarkCnt'] = result['remarkCnt']
            item['content'] = result['content']
            item['source'] = result['source']
            items.append(item)
            self.count += 1
            print '###########current parsed:', self.count

            yield item
