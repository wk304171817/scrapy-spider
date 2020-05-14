# -*- coding: utf-8 -*-
import scrapy
import re

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/974434485/profile']
    def start_requests(self):
        cookies = "anonymid=ka627b1otjbw1a; depovince=ZGQT; jebecookies=953a89be-afc3-477a-b2be-139fbe5a9827|||||; _r01_=1; JSESSIONID=abcsrt5gcXUKh5CZ_Qqix; ick_login=ff2953d1-4aa4-4a5f-9cd0-ea35a6943ce7; taihe_bi_sdk_uid=26f164bb39f1fdc76b3835b60b8bb5f7; taihe_bi_sdk_session=42a5b1da173996d23b68895000a4b76d; _de=FF3CF2304DB2C8C800BB013026607CE5; ick=ddbf8122-8956-40ff-ba2d-14a63b0319b7; t=f74670b8a4e402a83f94bb89ab2f755b5; societyguester=f74670b8a4e402a83f94bb89ab2f755b5; id=974434485; xnsid=ef50687f; ver=7.0; loginfrom=null; jebe_key=1e392101-6a72-4d09-ab3a-9efc99b78eed%7C505b00be56c3ceed7e4b0792ac399f41%7C1589418024564%7C1%7C1589418025792; jebe_key=1e392101-6a72-4d09-ab3a-9efc99b78eed%7C505b00be56c3ceed7e4b0792ac399f41%7C1589418024564%7C1%7C1589418025794; _ga=GA1.2.944613912.1589418996; _gid=GA1.2.849437351.1589418996; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback= self.parse,
            cookies=cookies
        )

    def parse(self, response):
        #a = re.findall('王凯',response.body.decode())
        A= response.xpath('//ul[@class="fd-nav-list clearfix"]/li[2]/a/@href').extract_first()
        print('*'*20,A)
        #print(a)
        # cookies = 'anonymid=ka627b1otjbw1a; depovince=ZGQT; jebecookies=d1f421bc-4df8-49ee-bee2-26de3a0b8137|||||; _r01_=1; ick_login=ff2953d1-4aa4-4a5f-9cd0-ea35a6943ce7; taihe_bi_sdk_uid=26f164bb39f1fdc76b3835b60b8bb5f7; taihe_bi_sdk_session=42a5b1da173996d23b68895000a4b76d; _de=FF3CF2304DB2C8C800BB013026607CE5; ick=ddbf8122-8956-40ff-ba2d-14a63b0319b7; t=f74670b8a4e402a83f94bb89ab2f755b5; societyguester=f74670b8a4e402a83f94bb89ab2f755b5; id=974434485; xnsid=ef50687f; ver=7.0; loginfrom=null; jebe_key=1e392101-6a72-4d09-ab3a-9efc99b78eed%7C505b00be56c3ceed7e4b0792ac399f41%7C1589418024564%7C1%7C1589418025792;JSESSIONID=abczRzM9hFpox5qxsWqix; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1589418995,1589419079; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1589419079; _ga=GA1.2.944613912.1589418996; _gid=GA1.2.849437351.1589418996; _ga=GA1.3.944613912.1589418996; _gid=GA1.3.849437351.1589418996'
        # cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            A,
            callback=self.parse1,
        )
    def parse1(self,response):
        a = response.xpath('//div[@class = "info-section-info"]/dl[4]/dd/a/text()').extract()
        print(a)

        #
        # li_list = response.xpath('//ul[@class="list hot-list"]/li')
        # for li in li_list:
        #     item = {}
        #     item['name'] = li.xpath('./li/div[@class="live-info"]/p[2]/text()').extract_first()
        #     item["title"] = li.xpath('./li/div[@class="live-info"]/p[1]/text()').extract_first()
        #     print(item)