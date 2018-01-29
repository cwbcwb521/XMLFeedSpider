# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyxmlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 存储文章标题
    title = scrapy.Field()
    # 存储对应连接
    link = scrapy.Field()
    # 存储对应文章作者
    author = scrapy.Field()
