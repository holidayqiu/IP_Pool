# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IPinfo(scrapy.Item):
    addr=scrapy.Field()
    port=scrapy.Field()
    location=scrapy.Field()
    is_uknow=scrapy.Field()
    type=scrapy.Field()
    speed=scrapy.Field()
    connect_time=scrapy.Field()
    survival=scrapy.Field()
    proving_date=scrapy.Field()
    pass
