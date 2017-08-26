# -*- coding:utf8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import (BiliVideoDetailViewSet, BiliUperlViewSet, BiliDatalViewSet)

router = DefaultRouter()
router.register(r'video', BiliVideoDetailViewSet, base_name='video')
router.register(r'uper', BiliUperlViewSet, base_name='uper')
router.register(r'data', BiliDatalViewSet, base_name='data')

urlpatterns = [
    # video api
    url(r'', include(router.urls)),
]
