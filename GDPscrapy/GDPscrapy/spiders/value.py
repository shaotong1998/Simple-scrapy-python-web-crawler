# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import GdpscrapyItem

class ValueSpider(scrapy.Spider):
    name = 'value'
    allowed_domains = ['kylc.com']
    start_urls = ['https://www.kylc.com/stats/global/yearly/g_gdp/1960.html']

    #年份解析函数
    def parse(self, response):
        #提取本页内除60年外的连接
        le = LinkExtractor(restrict_css='html body div.container div.container div.row div.col-md-3 div.panel.panel-default div.panel-body ul.list-inline.ul-year')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_value)



    #信息解析函数
    def parse_value(self,response):
        #GDP = GdpscrapyItem()
        val = response.css('html body div.container div.container div.row div.col-md-9 div.row div.panel.panel-default div.table-responsive table.table tbody')
        #/html/body/div[2]/div[1]/div[5]/div[1]/div/div/div/table/tbody
        year = response.xpath('/html/body/div[2]/div[1]/div[3]/div/h3/text()').extract_first()
        yearcut = re.sub("\D","",year)

        for p in val.xpath('./tr'):
            GDP = GdpscrapyItem()
            GDP['country'] =p.xpath('./td[2]/text()').extract_first()
            GDP['value'] = p.xpath('./td[4]/text()').extract_first()
            GDP['time'] = yearcut
            GDP['proportion'] = p.xpath('./td[5]/text()').extract_first()
            GDP['rank'] = p.xpath('./td[1]/text()').extract_first()
            GDP['zhou'] =p.xpath('./td[3]/text()').extract_first()
            yield GDP
