# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import redis
import datetime
from scrapy import signals
import re
import json
import codecs
import logging
from collections import OrderedDict
from base.import_django_model import *
from movies.models import Movies

key_list = ['title', 'url', 'bg_img_url_list']


class JsonWithEncodingPipeline(object):
    def __init__(self):
        # self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        items = OrderedDict(item)
        self.save_item(items)
        print('saved: %d' % len(items))
        # self.file.write(line)
        return item

    def close_spider(self, spider):
        # self.file.close()
        pass

    @classmethod
    def save_item(cls, items):
        url_list = items['url']
        bg_img_url_list = items['bg_img_url']
        title_list = items['title']

        movies_list = []
        movies_saved = []
        for i in xrange(len(title_list)):
            try:
                title = title_list[i]
                if title in movies_saved:
                    continue
                url = url_list[i]
                if url.startswith('//'):
                    url = 'http:%s' % url

                r = re.findall(r'id_([\S]+)\.html', url.split('/')[-1])
                source_id = ''
                if r:
                    source_id = r[0]
                # 去重
                is_exists = False
                if source_id:
                    m = Movies.objects.filter(source_id=source_id)
                    if m.exists():
                        is_exists = True
                else:
                    m = Movies.objects.filter(title=title)
                    if m.exists():
                        is_exists = True

                if is_exists:
                    m = m[0]
                else:
                    m = Movies()

                m.title = title
                m.url = url
                m.bg_img_url = bg_img_url_list[i]
                m.source_id = source_id
                m.update_at = datetime.datetime.now()

                if is_exists:
                    m.save()
                else:
                    movies_list.append(m)
                movies_saved.append(title)
            except Exception as e:
                logging.error(e)

        Movies.objects.bulk_create(movies_list)


class RedisPipeline(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379)

    def process_item(self, item, spider):
        if not item['id']:
            print 'no id item!!'

        str_recorded_item = self.r.get(item['id'])
        final_item = None
        if str_recorded_item is None:
            final_item = item
        else:
            ritem = eval(self.r.get(item['id']))
            final_item = dict(item.items() + ritem.items())
        self.r.set(item['id'], final_item)

    def close_spider(self, spider):
        return
