# coding=utf-8
import json
import scrapy

from wordBookSpider.items import PhraseItem


class PhraseSpider(scrapy.Spider):
    name = "phrase"
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
        # 常用短语
        phraseList = response.xpath('//*[@class="layout phrase"]/dl')
        for dl in phraseList:
            phrase = PhraseItem()
            phrase['word'] = response.meta['word']
            phrase['phrase'] = dl.xpath('dt/b/text()').extract_first().replace('\n', '').replace('\t', '')
            phrase['desc'] = dl.xpath('dd/ol/text()').extract_first().replace('\n', '').replace('\t', '')
            print phrase
            yield phrase
        # 词汇搭配
        phraseList = response.xpath('//*[@class="layout coll"]/ul/li')
        for li in phraseList:
            phrase = PhraseItem()
            phrase['word'] = response.meta['word']
            phrase['phrase'] = li.xpath('a/text()').extract_first().replace('\n', '').replace('\t', '')
            phrase['desc'] = li.xpath('./text()').extract()[1].replace('\n', '').replace('\t', '')
            print phrase
            yield phrase