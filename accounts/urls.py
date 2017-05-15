# -*- coding:utf8 -*-
from django.conf.urls import patterns, url
from .views import (LoginView, LogoutView)

urlpatterns = patterns('accounts.views',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LoginView.as_view(), name='logout'),
)
