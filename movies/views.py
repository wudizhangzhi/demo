# -*- coding:utf8 -*-
from django.views.generic.base import TemplateView


class TestView(TemplateView):
    template_name = 'movies/test.html'

    def get_context_data(self, **kwargs):
        return super(TestView, self).get_context_data(**kwargs)
