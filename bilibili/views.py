# -*- coding:utf8 -*-

from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BiliVideo



class BiLiVideoView(TemplateView):
    # 哔哩哔哩视频页面
    model = BiliVideo
    template_name = 'bilibili/bilivideo.html'
    # def get(self, request, *args, **kwargs):
    #     return super(BiLiVideoView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(BiLiVideoView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)
        pagesize = self.request.GET.get('pagesize', 20)
        # videolist = BiliVideo.objects.all()[page:pagesize]
        paginator = Paginator(BiliVideo.objects.all(), pagesize)
        try:
            videolist = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            videolist = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            videolist = paginator.page(paginator.num_pages)
        context_data['videolist'] = videolist
        return context_data


class TestView(TemplateView):
    template_name = 'bilibili/index.html'
    def get_context_data(self, **kwargs):
        return super(TestView, self).get_context_data(**kwargs)
