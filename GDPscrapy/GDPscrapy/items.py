# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GdpscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field() #国家
    value = scrapy.Field() #GDP数据
    time = scrapy.Field() #年份
    proportion = scrapy.Field() #当年GDP数据占比
    rank = scrapy.Field() #排名
    zhou = scrapy.Field()#洲名
