# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class YhdSpider(scrapy.Spider):
    name = 'yhd'
    allowed_domains = ['yhd.com']
    start_urls = ['https://search.yhd.com/c1343-0-0/mbname-b/a-s1-v0-p1-price-d0-f0-m1-rt0-pid-mid0-color-size-k']

    def parse(self, response):
        a_list = response.xpath('//ul[@class="guide_con clearfix"]/li/div/a')
        for a in a_list:
            item = {}
            item['url'] = a.xpath('./@href').extract_first()
            item['url'] = 'https:' + item['url']
            item['title'] = a.xpath('./text()').extract_first()
            print(item['url'])

            yield scrapy.Request(
                item['url'],
                callback= self.parse1,
                meta= {"item":deepcopy(item)}
            )
    def parse1(self,response):
        item = response.meta['item']
        mod_list = response.xpath('//div[@id="itemSearchList"]/div')
        for mod in mod_list:
            item['l_title'] = mod.xpath('./div/p[@class="proName clearfix"]/a/@title').extract_first()
            item['price'] = mod.xpath('./div/p[@class="proPrice"]/em/@yhdprice').extract_first()
            item['img'] = mod.xpath('./div/div[@id="searchProImg"]/a/div/img/@original').extract_first()
            if mod.xpath('./div/div[@id="searchProImg"]/a/div/img/@original').extract_first() is None:
                item['img'] = mod.xpath('./div/div[@id="searchProImg"]/a/div/img/@src').extract_first()
            if item['img'] is None:
                item['img'] =  mod.xpath('./div/div[@id="searchProImg"]/a/img/@src').extract_first()
            item['url1'] = mod.xpath('./div/div[@id="searchProImg"]/a/@href').extract_first()
            item['url1'] = 'https:'+ item['url1']
            print(item)

