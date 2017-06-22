# coding=utf-8
import json

import scrapy

from wordBookSpider.items import SentenceItem


class PhraseSpider(scrapy.Spider):
    name = "sentence"
    allowed_domains = ["dict.cn"]

    def start_requests(self):
        # word = "try"
        # url = 'http://dict.cn/%s' % word
        # yield scrapy.Request(url, meta={'word': word}, callback=self.parse)

        file = open("wordBookSpider/word.json")

        for line in file:
            wordObj = json.loads(line)
            word = wordObj["word"]
            if word:
                url = 'http://dict.cn/%s' % word
                print url
                # yield scrapy.Request(url, meta={'word': word}, callback=self.parse)
            else:
                continue

    def parse(self, response):
        # 例句
        sentenceList = response.xpath('//*[@class="layout sort"]/ol/li')
        for li in sentenceList:
            sentence = SentenceItem()
            sentence['word'] = response.meta['word']
            sentence['sentence'] = li.xpath('./text()').extract_first().replace('\n', '').replace('\t', '')
            sentence['desc'] = li.xpath('./text()').extract()[1].replace('\n', '').replace('\t', '')
            print sentence
            yield sentence

        # 常见句型
        sentenceList = response.xpath('//*[@class="layout patt"]/ol/li')
        for li in sentenceList:
            sentence = SentenceItem()
            sentence['word'] = response.meta['word']
            sentence['sentence'] = li.xpath('./text()').extract_first().replace('\n', '').replace('\t', '')
            sentence['desc'] = li.xpath('./text()').extract()[1].replace('\n', '').replace('\t', '')
            print sentence
            yield sentence