# -*- coding:utf8 -*-
from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    '',
    # bilibili api
    url(r'^bilibili/', include('bilibili.rest.urls')),
    )
