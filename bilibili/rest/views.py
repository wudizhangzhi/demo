# -*- coding:utf8 -*-
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
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
