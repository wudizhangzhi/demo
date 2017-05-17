# -*- coding:utf8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from .views import (BiLiVideoView, TestView, BiliDashboard,
                BiliVideoDetail, BiliUperView )




urlpatterns = patterns('bilibili.views',
    url(r'^$', BiliDashboard.as_view(), name='dashboard'),
    url(r'^videolist$', BiLiVideoView.as_view(), name='videolist'),
    url(r'^video/(?P<av_id>\d+)$', BiliVideoDetail.as_view(), name='video'),
    url(r'^uper/(?P<pk>\d+)$', BiliUperView.as_view(), name='uper'),
    url(r'^test/$', TestView.as_view(), name='test'),
)
