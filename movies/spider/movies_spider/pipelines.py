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
from movies.models import Movies, SubMovies


class JsonWithEncodingPipeline(object):
    def __init__(self):
        # self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')
        pass

    def process_item(self, item, spider):
        if 'bg_img_url' in item:
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
                    logging.debug(u'saved pass: %s' % title)
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
                    logging.debug(u'update %s' % title)
                    m.save()
                else:
                    logging.debug(u'save %s' % title)
                    movies_list.append(m)
                movies_saved.append(title)
            except Exception as e:
                logging.error(e)

        Movies.objects.bulk_create(movies_list)


class HandlerTvPipeline(object):


    def __init__(self):
        self.category = dict([(v, k) for k, v in Movies.CATEGORY])

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if 'category' in item:
            items = OrderedDict(item)
            # self.save_sub_item(items)
            # =========

            category = items['category'][0][1:-1]
            _category = self.category.get(category)
            if _category not in [Movies.TV, Movies.CARTOON]:
                print('not in list', _category)
                return item
            title = items['title'][0]
            logging.info(u'TV: %r' % title)

            sub_title_list = items['sub_title']
            seq_list = items['seq']
            url_list = items['url']
            seq_dict = dict([(seq, {'sub_title': sub_title, 'url': url}) for seq, sub_title, url in
                             zip(seq_list, sub_title_list, url_list)])
            if not seq_dict:
                print('not seq_dict')
                return item
            seq_not_exist_set = seq_list

            # 判断类型, 是否保存过
            m = Movies.objects.filter(category=_category, title=title)
            if m.exists():
                m = m[0]
            else:  # 创建
                m = Movies()
                m.title = title
                m.category = _category
                m.save()

                seq_set = set(seq_list)
                seq_exist_list = SubMovies.objects.filter(parent__pk=m.id, seq__in=seq_set).values_list('seq',
                                                                                                        flat=True)

                seq_not_exist_set = seq_set.difference(seq_exist_list)
                # TODO 更新

            # 保存
            sub_movies = []
            for seq in seq_not_exist_set:
                sm = SubMovies()
                sm.seq = seq
                sm.title = seq_dict[seq]['sub_title']
                sm.url = seq_dict[seq]['url']
                sm.parent = m
                sub_movies.append(sm)

                logging.debug(u'save: %s' % seq_dict[seq]['sub_title'])

            SubMovies.objects.bulk_create(sub_movies)

            # =========
        return item

    @classmethod
    def save_sub_item(cls, items):
        try:
            category = items['category'][0]
            _category = HandlerTvPipeline.category.get(category)
            if _category not in [Movies.TV, Movies.CARTOON]:
                yield
            title = items['title'][0]

            sub_title_list = items['sub_title']
            seq_list = items['seq']
            url_list = items['url']
            seq_dict = dict([(seq, {'sub_title': sub_title, 'url': url}) for seq, sub_title, url in
                             zip(seq_list, sub_title_list, url_list)])
            seq_not_exist_set = seq_list

            # 判断类型, 是否保存过
            m = Movies.objects.filter(category=_category, title=title)
            if not m.exists():  # 创建
                m = Movies()
                m.title = title
                m.category = category
                m.save()

                seq_set = set(seq_list)
                seq_exist_list = SubMovies.objects.filter(parent__pk=m.id, seq__in=seq_set).values_list('seq',
                                                                                                        flat=True)

                seq_not_exist_set = seq_set.difference(seq_exist_list)
                # TODO 更新

            # 保存
            sub_movies = []
            for seq in seq_not_exist_set:
                sm = SubMovies()
                sm.seq = seq
                sm.title = seq_dict[seq]['sub_title']
                sm.url = seq_dict[seq]['url']
                sub_movies.append(sm)

            SubMovies.objects.bulk_create(sub_movies)
            print('saved %s' % len(sub_movies))

        except Exception, e:
            logging.error(e)
            print(e)


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
