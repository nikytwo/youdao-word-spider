# -*- coding: utf-8 -*-
import scrapy

from wordBookSpider.items import WordItem


class WordSpider(scrapy.Spider):
    name = "word"
    allowed_domains = ["youdao.com"]
    start_urls = [
        "http://dict.youdao.com/wordbook/wordlist"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies={
                'DICT_LOGIN': '1||1496736356740',
                'DICT_SESS': 'v2|URSM|DICT||nikytwo@163.com||urstoken||N0DbcAVj8l5mlYT8jT17YURVeF9rasVU3fJNCCGLRu1h8Ftg8d_0OT4KHBGcUlFxfAr497YXJ65GNGCVozoNAEfgR2l8Bg_QE6E65PBt_8UvU_3PFGM8iDAZ7ezsPMJUZLFfgKxe2mEycJry8ZHjPCH5E25RUDozmeLfgXEKoOqtwRjmsWZ8YUR7bas8rgwil||604800000||pKOLPKOMTBRlMP4Ju0LkY0Q4P4gLPMpLRwuhHPFkfqu0guhMUA6MQ40lY0HYEOfJF0lWP4PKOfkm0gFRLYfh4JuR'
            })

    def parse(self, response):
        page = response.xpath('//*[@class="current-page"]/text()').extract()
        print page
        trs = response.xpath('//tbody/tr')
        for tr in trs:
            word = WordItem()
            word['word'] = tr.xpath('td[2]/div/a/strong/text()').extract_first()
            word['phonetic'] = tr.xpath('td[3]/div/text()').extract_first()
            word['desc'] = tr.xpath('td[4]/div/text()').extract_first()
            word['tags'] = tr.xpath('td[6]/div/text()').extract_first()
            word['date'] = tr.xpath('td[5]/text()').extract_first()
            yield word

        links = response.css('.next-page')
        url = 'http://dict.youdao.com/wordbook/%s' % links[0].xpath('@href').extract_first()
        print url
        # yield scrapy.Request(url, self.parse)
