# -*- coding:utf8 -*-
from django.conf.urls import url, include
from .views import (TestView)

urlpatterns = [
    url(r'^test$', TestView.as_view(), name='dashboard'),
]
