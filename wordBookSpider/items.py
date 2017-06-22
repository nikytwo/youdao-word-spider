# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WordItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    word = scrapy.Field()
    phonetic = scrapy.Field()
    desc = scrapy.Field()
    tags = scrapy.Field()
    date = scrapy.Field()


class PhraseItem(scrapy.Item):
    word = scrapy.Field()
    phrase = scrapy.Field()
    desc = scrapy.Field()


class SentenceItem(scrapy.Item):
    word = scrapy.Field()
    sentence = scrapy.Field()
    desc = scrapy.Field()
