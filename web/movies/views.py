# -*- coding:utf8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from movies.models import Movies


class TestView(TemplateView):
    template_name = 'movies/test.html'

    def get_context_data(self, **kwargs):
        return super(TestView, self).get_context_data(**kwargs)


class IndexView(TemplateView):
    template_name = 'movies/index.html'

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)


class PlayView(TemplateView):
    template_name = 'movies/play.html'

    def get_context_data(self, **kwargs):
        v = self.request.GET.get('v', '')
        context = super(PlayView, self).get_context_data(**kwargs)
        context['v'] = v
        return context


class MainView(TemplateView):
    template_name = 'movies/main.html'

    def get_context_data(self, **kwargs):
        return super(MainView, self).get_context_data(**kwargs)


class TvView(TemplateView):
    template_name = 'movies/tv.html'

    def get_context_data(self, **kwargs):
        context = super(TvView, self).get_context_data(**kwargs)
        tvid = self.request.GET.get('v', '')
        tvinfo = get_object_or_404(Movies, id=tvid)
        context['tvinfo'] = tvinfo
        return context
