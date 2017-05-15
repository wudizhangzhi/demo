# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BiliTag'
        db.create_table(u'bilibili_bilitag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('typeid', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('ctime', self.gf('django.db.models.fields.DateTimeField')()),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliTag'])

        # Adding model 'BiliTagData'
        db.create_table(u'bilibili_bilitagdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagdata', to_field='tag_id', to=orm['bilibili.BiliTag'])),
            ('use', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('atten', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_atten', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hates', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('attribute', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('liked', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hated', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliTagData'])

        # Adding model 'BiliVideoTag'
        db.create_table(u'bilibili_bilivideotag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videotags', to_field='aid', to=orm['bilibili.BiliVideo'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tagvideos', to_field='tag_id', to=orm['bilibili.BiliTag'])),
        ))
        db.send_create_signal(u'bilibili', ['BiliVideoTag'])

        # Adding model 'BiliVideo'
        db.create_table(u'bilibili_bilivideo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aid', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('uper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userid', to_field='uid', to=orm['bilibili.BiliUper'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('addtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('vdesc', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliVideo'])

        # Adding model 'BiliVideoData'
        db.create_table(u'bilibili_bilivideodata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='videodata', to_field='aid', to=orm['bilibili.BiliVideo'])),
            ('view', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('danmaku', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('reply', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('favorite', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('coin', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('share', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliVideoData'])

        # Adding model 'BiliUper'
        db.create_table(u'bilibili_biliuper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uid', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('sign', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('regtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('avatar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliUper'])

        # Adding model 'BiliUperData'
        db.create_table(u'bilibili_biliuperdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='upderdata', to_field='uid', to=orm['bilibili.BiliUper'])),
            ('videonum', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('gz', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('fans', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('play', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'bilibili', ['BiliUperData'])


    def backwards(self, orm):
        # Deleting model 'BiliTag'
        db.delete_table(u'bilibili_bilitag')

        # Deleting model 'BiliTagData'
        db.delete_table(u'bilibili_bilitagdata')

        # Deleting model 'BiliVideoTag'
        db.delete_table(u'bilibili_bilivideotag')

        # Deleting model 'BiliVideo'
        db.delete_table(u'bilibili_bilivideo')

        # Deleting model 'BiliVideoData'
        db.delete_table(u'bilibili_bilivideodata')

        # Deleting model 'BiliUper'
        db.delete_table(u'bilibili_biliuper')

        # Deleting model 'BiliUperData'
        db.delete_table(u'bilibili_biliuperdata')


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
            'gz': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'uper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'upderdata'", 'to_field': "'uid'", 'to': u"orm['bilibili.BiliUper']"}),
            'videonum': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        },
        u'bilibili.bilivideo': {
            'Meta': {'object_name': 'BiliVideo'},
            'addtime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'aid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'through': u"orm['bilibili.BiliVideoTag']", 'to': u"orm['bilibili.BiliTag']"}),
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