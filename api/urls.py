# -*- coding:utf8 -*-
from django.conf.urls import url, include


urlpatterns = [
    # bilibili api
    url(r'^bilibili/', include('bilibili.rest.urls')),
    ]
