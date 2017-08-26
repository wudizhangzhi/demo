# -*- coding:utf8 -*-
from django.conf.urls import url, include


urlpatterns = [
    # bilibili api
    url(r'^bilibili/', include('bilibili.rest.urls'), name='api-bilibili'),
    url(r'^movies/', include('movies.rest.urls'), name='api-movies'),
    ]
