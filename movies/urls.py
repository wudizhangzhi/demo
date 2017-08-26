# -*- coding:utf8 -*-


from django.conf.urls import url, include
from .views import (TestView, IndexView, PlayView)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^play/$', PlayView.as_view(), name='play'),

]
