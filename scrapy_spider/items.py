# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    createTime = scrapy.Field()
    remarkCnt = scrapy.Field()
    source = scrapy.Field()
    pass
