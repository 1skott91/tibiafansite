# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TibiaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    vocation = scrapy.Field()
    level = scrapy.Field()
    exp = scrapy.Field()
    pass
