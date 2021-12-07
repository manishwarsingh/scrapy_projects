# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

def remove_whitespaces(value):
    return value.replace('\u00a0, \xa0',' ').strip()


class QuickFactsItem(scrapy.Item):
    # define the fields for your item here like:
    questions        = scrapy.Field()
    tags             = scrapy.Field()
    soluction        = scrapy.Field()
    post_tags        = scrapy.Field()
    auther_name_href = scrapy.Field()
    auther_name      = scrapy.Field()

    
