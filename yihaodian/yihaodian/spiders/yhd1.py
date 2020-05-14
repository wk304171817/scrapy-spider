# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Yhd1Spider(CrawlSpider):
    name = 'yhd1'
    allowed_domains = ['yhd.com']
    start_urls = ['https://search.yhd.com/c9719-0-0/mbname-b/a-s1-v0-p1-price-d0-f0-m1-rt0-pid-mid0-color-size-k/']

    rules = (
        Rule(LinkExtractor(
            allow=r'//item\.yhd.com/\d+\.html'),
             callback='parse_item'),
    )
    #linkExtractor 链接提取器   parse 函数不能定义 有特殊功能   follow 当前url的响应是否继续用 当前rule 继续提取url
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['title'] = response.xpath('//img[@id="J_prodImg"]/@src').extract()


        print(item)

