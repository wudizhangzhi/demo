# encoding: utf-8
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import viewsets, status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import *
from movies.serializers import MoviesShowSerializers, TvShowSerializers


class MoviesViewSet(viewsets.ModelViewSet):
    page_size = 20
    serializer_class = MoviesShowSerializers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        seach = self.request.GET.get('search', '')
        if seach:
            queryset = Movies.objects.filter(title__startswith=seach).order_by('update_at')
        else:
            queryset = Movies.objects.all().order_by('update_at')
        return queryset


class TvViewSet(viewsets.ModelViewSet):
    page_size = 20
    serializer_class = TvShowSerializers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        v = self.request.GET.get('v', '')
        if not v:
            raise Http404
        else:
            queryset = SubMovies.objects.filter(parent__id=v).exclute(category=Movies.MOVIE).order_by('seq')
        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response(data={'status': 1})


