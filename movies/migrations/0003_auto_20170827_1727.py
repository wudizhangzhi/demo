# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170826_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.IntegerField(choices=[(0, b'\xe7\x94\xb5\xe5\xbd\xb1'), (1, b'\xe7\x94\xb5\xe8\xa7\x86\xe5\x89\xa7'), (2, b'\xe7\xbb\xbc\xe8\x89\xba')], default=0),
        ),
        migrations.AlterField(
            model_name='movies',
            name='film_type',
            field=models.IntegerField(choices=[(0, b'\xe6\xad\xa3\xe7\x89\x87'), (1, b'\xe9\xa2\x84\xe5\x91\x8a')], default=0),
        ),
    ]
