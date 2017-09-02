# coding=utf8
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Movies(models.Model):
    YOUKU = 0
    SOURCE_TYPE = (
        (YOUKU, _('youku')),
    )
    WHOLE = 0  # 正片
    TRAILER = 1  # 预告
    FILM_TYPE = (
        (WHOLE, '正片'),
        (TRAILER, '预告'),
    )

    MOVIE = 0  # 电影
    TV = 1  # 电视剧
    ZONGYI = 2  # 综艺
    CARTOON = 3  # 卡通
    CATEGORY = (
        (MOVIE, u'电影'),
        (TV, u'剧集'),
        (ZONGYI, u'综艺'),
        (CARTOON, u'动漫'),
    )

    title = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    bg_img_url = models.TextField(blank=True, null=True)  # 电影海报
    director = models.CharField(max_length=255, blank=True, null=True)
    lead_actor = models.CharField(max_length=255, blank=True, null=True)
    from_at = models.CharField(max_length=100, blank=True, null=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)  # 上映年份
    op_type = models.CharField(max_length=255, blank=True, null=True)  # 电影类型
    film_type = models.IntegerField(choices=FILM_TYPE, default=WHOLE)  # 是否正片等
    category = models.IntegerField(choices=CATEGORY, default=MOVIE)  # 资源类型

    tags = models.ManyToManyField('movies.MovieTags')  #
    summary = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    source_type = models.IntegerField(choices=SOURCE_TYPE, default=YOUKU, blank=True, null=True)  # 来源
    source_key = models.CharField(max_length=255, blank=True, null=True)
    source_id = models.CharField(max_length=255, blank=True, null=True)

    # video_id = models.CharField(max_length=255, blank=True, null=True)  # youku video_id

    def __unicode__(self):
        return self.title


class MovieTags(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class SubMovies(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField(blank=False)
    seq = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('movies.Movies', related_name='subs')

    def __unicode__(self):
        return self.title