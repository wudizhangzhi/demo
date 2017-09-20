# encoding: utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from movies.rest.views import (MoviesViewSet, TvViewSet)

router = DefaultRouter()
router.register(r'movies', MoviesViewSet, base_name='movies')
router.register(r'tv', TvViewSet, base_name='tvs')

urlpatterns = [
    # video api
    url(r'', include(router.urls)),
]
