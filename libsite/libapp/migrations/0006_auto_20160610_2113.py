# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 21:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0005_auto_20160525_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='libuser',
            name='photo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 10)),
        ),
        migrations.AlterField(
            model_name='libitem',
            name='duedate',
            field=models.DateField(default=datetime.date(2016, 7, 1), null=True),
        ),
    ]
