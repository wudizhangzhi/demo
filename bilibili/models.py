# -*- coding:utf8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class BiliVideo(models.Model):
    aid = models.IntegerField(null=False, verbose_name=_("avid")) # avid
    # TODO 修改为 models.ForeignKey()
    mid = models.IntegerField(null=False, verbose_name=_("up's id")) # up主
    url = models.CharField(max_length=255, blank=False) # url
    title = models.CharField(max_length=255, blank=False) # 标题
    view = models.IntegerField(null=True, verbose_name=_("view num")) # 总播放数量
    danmaku = models.IntegerField(null=True, verbose_name=_("danmu num")) # 总弹幕数量
    reply = models.IntegerField(null=True, verbose_name=_("reply num")) # 评论数量
    favorite = models.IntegerField(null=True) # 收藏
    coin = models.IntegerField(null=True) # 硬币
    share = models.IntegerField(null=True) # 分享
