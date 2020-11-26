# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import  re
class GdpscrapyPipeline(object):
    def process_item(self, item, spider):
        return item

#定义要求的value格式
class ValuePipeline(object):
    def process_item(self,item,spider):

        str = item['value']
        meth = re.compile(r'[(](.*?)[)]',re.S)
        str1 = re.findall(meth,str)
        str2 = str1[0].replace(',','')
        item['value'] = str2

        return item


#选定前30名的国家，并取消选中世界和欧盟！
class TopPipeline(object):
    def process_item(self,item,spider):

        str  = item['rank']
        a = int(str)
        if a>=250:
            raise DropItem()
        elif a=='':
            raise DropItem()

        return item




