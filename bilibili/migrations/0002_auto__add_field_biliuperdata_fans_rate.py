# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BiliUperData.fans_rate'
        db.add_column(u'bilibili_biliuperdata', 'fans_rate',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BiliUperData.fans_rate'
        db.delete_column(u'bilibili_biliuperdata', 'fans_rate')


    models = {
        u'bilibili.bilitag': {
            'Meta': {'object_name': 'BiliTag'},
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ctime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'typeid': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'bilibili.bilitagdata': {
            'Meta': {'object_name': 'BiliTagData'},
            'atten': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'attribute': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'hated': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hates': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_atten': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'liked': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagdata'", 'to_field': "'tag_id'", 'to': u"orm['bilibili.BiliTag']"}),
            'use': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'bilibili.biliuper': {
            'Meta': {'object_name': 'BiliUper'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'regtime': ('django.db.models.fields.DateTimeField', [], {}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'bilibili.biliuperdata': {
            'Meta': {'object_name': 'BiliUperData'},
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fans': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'fans_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'gz': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'uper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uperdata'", 'to_field': "'uid'", 'to': u"orm['bilibili.BiliUper']"}),
            'videonum': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        },
        u'bilibili.bilivideo': {
            'Meta': {'object_name': 'BiliVideo'},
            'addtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'aid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'video'", 'symmetrical': 'False', 'through': u"orm['bilibili.BiliVideoTag']", 'to': u"orm['bilibili.BiliTag']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userid'", 'to_field': "'uid'", 'to': u"orm['bilibili.BiliUper']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vdesc': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'bilibili.bilivideodata': {
            'Meta': {'object_name': 'BiliVideoData'},
            'coin': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'danmaku': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'favorite': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reply': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'share': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videodata'", 'to_field': "'aid'", 'to': u"orm['bilibili.BiliVideo']"}),
            'view': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'bilibili.bilivideotag': {
            'Meta': {'object_name': 'BiliVideoTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagvideos'", 'to_field': "'tag_id'", 'to': u"orm['bilibili.BiliTag']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videotags'", 'to_field': "'aid'", 'to': u"orm['bilibili.BiliVideo']"})
        }
    }

    complete_apps = ['bilibili']