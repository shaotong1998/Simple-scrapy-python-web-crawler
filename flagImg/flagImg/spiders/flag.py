# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import FlagimgItem
class FlagSpider(scrapy.Spider):
    name = 'flag'
    allowed_domains = ['ivsky.com']
    start_urls = ['https://www.ivsky.com/tupian/geguo_guoqi_v1773/']
    i = 10

    def parse(self, response):
    #提取单个页面中每个国旗的链接
        le = LinkExtractor(restrict_css='html body div.box div.left ul.pli')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_img)
    #提取下一页的连接
        le = LinkExtractor(restrict_css='html body div.box div.left div.page_c div.pagelist a')
        links = le.extract_links(response)
        i =self.i
        if links:
            next_url = links[i].url
            self.i = 11
            yield scrapy.Request(next_url,callback=self.parse)



    def parse_img(self,response):
        url = response.xpath('//*[@id="imgis"]/@src').extract()
        item =FlagimgItem()
        reurl = "http:"+url[0]

        list=[]
        list.append(reurl)
        print(list[0])
        item['img_url']=list[0]


        yield item
        #提交到管道
        #return item


