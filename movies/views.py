# -*- coding:utf8 -*-
from django.views.generic.base import TemplateView


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