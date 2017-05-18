# -*- coding:utf8 -*-
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, detail_route, list_route
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Count, Max
from bilibili.models import *

import datetime

class BiliVideoDetailViewSet(viewsets.ViewSet):
    model = BiliVideo
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({'status':1})

    @action(methods=['GET'])
    def recent_week(self, request, pk=None):
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=7)
        videodata = BiliVideoData.objects.select_related().filter(video__pk=pk)
        class RecentWeekVideSeerializers(serializers.ModelSerializer):
            title = serializers.SerializerMethodField('get_title')
            createtime = serializers.SerializerMethodField('get_createtime')
            def get_title(self, obj):
                return obj.video.title

            def get_createtime(self, obj):
                return obj.createtime.date()

            class Meta:
                model = BiliVideoData

        return Response(data=RecentWeekVideSeerializers(videodata, many=True).data,
                status=status.HTTP_200_OK)


class BiliUperlViewSet(viewsets.ViewSet):
    model = BiliUperData
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response({'status':1})

    @action(methods=['GET'])
    def recent_week(self, request, pk=None):
        today = datetime.date.today()
        start_date = today - datetime.timedelta(days=7)
        videodata = BiliUperData.objects.select_related().filter(uper__pk=pk)
        class RecentWeekUperSeerializers(serializers.ModelSerializer):
            createtime = serializers.SerializerMethodField('get_createtime')

            def get_createtime(self, obj):
                return obj.createtime.date()

            class Meta:
                model = BiliUperData
                fields = ['videonum', 'gz', 'fans', 'play', 'createtime']

        return Response(data=RecentWeekUperSeerializers(videodata, many=True).data,
                status=status.HTTP_200_OK)


class BiliDatalViewSet(viewsets.ViewSet):
    model = BiliUperData
    permission_classes = [IsAuthenticated]
    def list(self, request):
        return Response({'status':1})

    @list_route()
    def uper_top(self, request):
        pagesize = request.GET.get('size', 5)
        uper_top = BiliUperData.objects.values('uper').\
        annotate(fans=Max('fans')).order_by('-fans')[:pagesize]
        class TopTenUperSeerializers(serializers.ModelSerializer):
            name = serializers.SerializerMethodField('get_name')
            uper_id = serializers.SerializerMethodField('get_uper_id')
            def get_name(self, obj):
                return BiliUper.objects.get(uid=obj['uper']).name or 'NULL'

            def get_uper_id(self, obj):
                return obj['uper']

            class Meta:
                model = BiliUperData
                fields = ['uper_id', 'fans', 'name']
        return Response(data=TopTenUperSeerializers(uper_top, many=True).data)

    @list_route()
    def video_top(self, request):
        pagesize = request.GET.get('size', 5)
        video_top = BiliVideoData.objects.values('video').\
        annotate(view=Max('view')).order_by('-view')[:pagesize]
        class TopTenUperSeerializers(serializers.ModelSerializer):
            title = serializers.SerializerMethodField('get_title')
            video_id = serializers.SerializerMethodField('get_video_id')
            def get_title(self, obj):
                return BiliVideo.objects.get(aid=obj['video']).title or 'NULL'

            def get_video_id(self, obj):
                return obj['video']

            class Meta:
                model = BiliVideoData
                fields = ['video_id', 'view', 'title']
        return Response(data=TopTenUperSeerializers(video_top, many=True).data)
