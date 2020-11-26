# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class FlagimgPipeline(object):
    def process_item(self, item, spider):
        return item


#重新图片下载类
class MyImagePipline(ImagesPipeline):
    #接收item对象并将获取的item对象的url发请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])


    def item_completed(self, results, item, info):
        return item

    def file_path(self, request, response=None, info=None):
        #给图片重命名，包含后缀名
        image_guid = request.url.split('/')[-1]
        return image_guid
