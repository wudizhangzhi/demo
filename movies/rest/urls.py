# encoding: utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from movies.rest.views import (MoviesViewSet)

router = DefaultRouter()
router.register(r'', MoviesViewSet, base_name='movies')

urlpatterns = [
    # video api
    url(r'', include(router.urls)),
]
