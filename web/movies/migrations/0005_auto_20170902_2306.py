# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20170828_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='category',
            field=models.IntegerField(choices=[(0, '\u7535\u5f71'), (1, '\u5267\u96c6'), (2, '\u7efc\u827a'), (3, '\u52a8\u6f2b')], default=0),
        ),
        migrations.AlterField(
            model_name='movies',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
