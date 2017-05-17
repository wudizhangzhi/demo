# -*- coding:utf8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import LoginRequiredMixin, JSONResponseMixin, \
    AjaxResponseMixin

from .models import *

import datetime



class BiLiVideoView(LoginRequiredMixin, TemplateView):
    # 哔哩哔哩视频页面
    model = BiliVideo
    template_name = 'bilibili/bilivideo.html'
    # def get(self, request, *args, **kwargs):
    #     return super(BiLiVideoView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(BiLiVideoView, self).get_context_data(**kwargs)
        page = int(self.request.GET.get('page', 1))
        pagesize = int(self.request.GET.get('pagesize', 20))
        # videolist = BiliVideo.objects.all()[page:pagesize]
        paginator = Paginator(BiliVideo.objects.all().order_by('-addtime'), pagesize)
        try:
            videolist = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            videolist = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            videolist = paginator.page(paginator.num_pages)
        page_total = paginator.num_pages
        startpagenum = (page - 6 < 1) and 1 or (page - 6)
        endpagenum = (startpagenum + 9 > page_total) and page_total or startpagenum + 9
        context_data['videolist'] = videolist
        context_data['pagelist'] = [i for i in xrange(startpagenum, endpagenum + 1)]
        context_data['page_cur'] = page
        context_data['pagesize'] = pagesize
        return context_data


class BiliDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'bilibili/dashboard.html'
    def get_context_data(self, *args, **kwargs):
        context_data = super(BiliDashboard, self).get_context_data(*args, **kwargs)

        today = datetime.date.today()
        # 视频数量
        video_total = BiliVideo.objects.all().count()
        # 今日上传视屏数量
        video_today = BiliVideo.objects.filter(addtime__gte=today).count()
        # uper数量
        uper_total = BiliUper.objects.all().count()
        # 今日新增uper数据的数量
        uper_today = BiliUper.objects.filter(createtime__gte=today).count()
        context_data['video_total'] = video_total
        context_data['video_today'] = video_today
        context_data['uper_total'] = uper_total
        context_data['uper_today'] = uper_today
        return context_data


class BiliVideoDetail(LoginRequiredMixin, TemplateView):
    template_name = 'bilibili/videodetail.html'
    def get(self, request, *args, **kwargs):
        return super(BiliVideoDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(BiliVideoDetail, self).get_context_data(**kwargs)
        av_id = kwargs.get('av_id', '')
        if not av_id:
            raise Http404()
        # today = datetime.date.today()
        # start_date = today - datetime.timedelta(days=7)
        # BiliVideoData.objects.filter(pk=av_id)
        taglist = BiliTag.objects.filter(video__pk=av_id).all()
        video = get_object_or_404(BiliVideo, pk=av_id)
        context_data['av_id'] = av_id
        context_data['taglist'] = taglist
        context_data['video'] = video
        return context_data


class BiliUperView(LoginRequiredMixin, TemplateView):
    template_name = 'bilibili/uper.html'
    def get(self, request, *args, **kwargs):
        return super(BiliUperView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(BiliUperView, self).get_context_data(**kwargs)
        pk = kwargs.get('pk', '')
        uper = get_object_or_404(BiliUper, pk=pk)
        context_data['uper'] = uper
        return context_data


class BiLiUperListView(LoginRequiredMixin, TemplateView):
    # 哔哩哔哩视频页面
    model = BiliUper
    template_name = 'bilibili/uperlist.html'
    # def get(self, request, *args, **kwargs):
    #     return super(BiLiVideoView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(BiLiUperListView, self).get_context_data(**kwargs)
        page = int(self.request.GET.get('page', 1))
        pagesize = int(self.request.GET.get('pagesize', 20))
        # videolist = BiliVideo.objects.all()[page:pagesize]
        paginator = Paginator(BiliVideo.objects.all().order_by('-addtime'), pagesize)
        try:
            videolist = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            videolist = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            videolist = paginator.page(paginator.num_pages)
        page_total = paginator.num_pages
        startpagenum = (page - 6 < 1) and 1 or (page - 6)
        endpagenum = (startpagenum + 9 > page_total) and page_total or startpagenum + 9
        context_data['videolist'] = videolist
        context_data['pagelist'] = [i for i in xrange(startpagenum, endpagenum + 1)]
        context_data['page_cur'] = page
        context_data['pagesize'] = pagesize
        return context_data


class TestView(TemplateView):
    template_name = 'bilibili/test.html'
    def get_context_data(self, **kwargs):
        return super(TestView, self).get_context_data(**kwargs)
