# encoding: utf-8

import re
import json

from scrapy.selector import Selector

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
    ]
    rules = [
        Rule(sle(allow=("list.youku.com/category/show/c_9[67]_?[_sdp0-9]+\.html")), callback='parse_1', follow=True),
    ]

    content_css_rules = {
        'title': 'div.p-thumb a::attr(title)',
        'url': 'div.p-thumb a::attr(href)',
        'bg_img_url': 'div.p-thumb img::attr(src)',
        # 'images': '#Cnt-Main-Article-QQ img::attr(src)',
        # 'images-desc': '#Cnt-Main-Article-QQ div p+ p::text',
    }

    def parse_1(self, response):
        # info('Parse ' + response.url)
        x = self.parse_with_rules(response, self.content_css_rules, dict)
        # print(json.dumps(x, ensure_ascii=False, indent=2))
        return x
        # return self.parse_with_rules(response, self.css_rules, hacker_newsItem)
