# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HellogithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #要爬取的字段名
    projectName=scrapy.Field()
    info=scrapy.Field()
