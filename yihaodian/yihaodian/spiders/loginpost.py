# -*- coding: utf-8 -*-
import scrapy


class LoginpostSpider(scrapy.Spider):
    name = 'loginpost'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
