# -*- coding:utf8 -*-
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from .views import (BiliVideoDetailViewSet, BiliUperlViewSet)

router = DefaultRouter()
router.register(r'video', BiliVideoDetailViewSet)
router.register(r'uper', BiliUperlViewSet)

urlpatterns = patterns(
    '',
    # video api
    url(r'', include(router.urls)),
    )
