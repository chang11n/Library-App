# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 06:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0009_auto_20160618_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 6, 18, 6, 37, 28, 650714, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
