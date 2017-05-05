# -*- coding:utf8 -*-
from django.conf.urls import patterns, url
from .views import BiLiVideoView, TestView

urlpatterns = patterns('bilibili.views',
    # url(r'', BiLiVideoView.as_view(), name='bilivideo'),
    url(r'^test/$', TestView.as_view(), name='test'),
)
