# -*- coding:utf8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.

class BiliTag(models.Model):
    name = models.CharField(max_length=255) #标签名称
    tag_id = models.IntegerField(unique=True, null=False)
    typeid = models.IntegerField(null=True)
    ctime = models.DateTimeField(null=False)
    createtime = models.DateTimeField(null=False, auto_now=True)
    def __unicode__(self):
        return self.name

class BiliTagData(models.Model):
    tag = models.ForeignKey(BiliTag, to_field='tag_id', related_name='tagdata')
    use = models.IntegerField(null=True)
    atten = models.IntegerField(null=True)
    is_atten = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    hates = models.IntegerField(null=True)
    attribute = models.IntegerField(null=True)
    liked = models.IntegerField(null=True)
    hated = models.IntegerField(null=True)
    createtime = models.DateTimeField(null=False, auto_now=True)


class BiliVideoTag(models.Model):
    video = models.ForeignKey('BiliVideo', to_field='aid', related_name='videotags')
    tag = models.ForeignKey(BiliTag, to_field='tag_id', related_name='tagvideos')

class BiliVideo(models.Model):
    aid = models.IntegerField(null=False, verbose_name=_("avid"), unique=True) # avid
    uper = models.ForeignKey('BiliUper', to_field='uid', related_name='userid') # up主
    url = models.CharField(max_length=255, blank=False) # url
    title = models.CharField(max_length=255, blank=False) # 标题
    createtime = models.DateTimeField(null=False) # 上传时间
    addtime = models.DateTimeField(auto_now=True) # 爬取的时间
    vdesc = models.TextField(null=True) #视频描述
    tags = models.ManyToManyField(BiliTag,
                                  through=BiliVideoTag,
                                  related_name='video')
    def __unicode__(self):
        return self.title

class BiliVideoData(models.Model):
    video = models.ForeignKey(BiliVideo, to_field='aid', related_name='videodata')
    view = models.IntegerField(null=True, verbose_name=_("view num")) # 总播放数量
    danmaku = models.IntegerField(null=True, verbose_name=_("danmu num")) # 总弹幕数量
    reply = models.IntegerField(null=True, verbose_name=_("reply num")) # 评论数量
    favorite = models.IntegerField(null=True) # 收藏
    coin = models.IntegerField(null=True) # 硬币
    share = models.IntegerField(null=True) # 分享
    createtime = models.DateTimeField(null=False, auto_now=True)

class BiliUper(models.Model):
    name = models.CharField(max_length=255)
    uid = models.IntegerField(null=False, unique=True)
    sign = models.CharField(max_length=255, null=True)
    regtime = models.DateTimeField() # 注册时间
    createtime = models.DateTimeField() # 创建时间
    # TODO 转换为ImageField()
    avatar = models.CharField(max_length=255, null=True)
    def __unicode__(self):
        return self.name

class BiliUperData(models.Model):
    uper = models.ForeignKey(BiliUper, to_field='uid', related_name='uperdata')
    videonum = models.IntegerField(null=True, default=0)
    gz = models.IntegerField(null=True, default=0) # 关注数
    fans = models.IntegerField(null=True, default=0)
    play = models.IntegerField(null=True, default=0) # 播放数量
    createtime = models.DateTimeField(null=False, auto_now=True)
