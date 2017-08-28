# encoding: utf-8

import re
import json

from scrapy.selector import Selector
import time

try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from ..items import *
from base.log import *
from base.spider import CommonSpider


class youku_Spider(CommonSpider):
    name = "movies_spider"
    allowed_domains = ["list.youku.com", "v.youku.com"]
    start_urls = [
        "http://list.youku.com/category/show/c_96.html",
        "http://list.youku.com/category/show/c_100.html",
    ]
    rules = [
        Rule(sle(allow=("list.youku.com/category/show/c_9[67]_?[_sdp0-9]*\.html")), callback='parse_1', follow=True),
        Rule(sle(allow=("http://v.youku.com/v_show/id_[\s+]+.html.*?")), callback='parse_tv', follow=True),
    ]

    # 列表页面用
    content_css_rules = {
        'title': 'div.p-thumb a::attr(title)',
        'url': 'div.p-thumb a::attr(href)',
        'bg_img_url': 'div.p-thumb img::attr(src)',
        # 'images': '#Cnt-Main-Article-QQ img::attr(src)',
        # 'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    # 播放页面用
    player_css_rules = {
        'category': 'h1.title a::text',
        'title': 'div.tvinfo h3::text',
        'sub_title': 'div.textlists div.lists div.items li.item::attr(title)',
        'seq': 'div.textlists div.lists div.items li.item::attr(seq)',
        'url': 'div.textlists div.lists div.items li.item a::attr(href)',

    }

    def parse_1(self, response):
        # info('Parse ' + response.url)
        x = self.parse_with_rules(response, self.content_css_rules, dict)
        # print(json.dumps(x, ensure_ascii=False, indent=2))
        return x

    def parse_tv(self, response):
        x = self.parse_with_rules(response, self.player_css_rules, dict)
        return x
