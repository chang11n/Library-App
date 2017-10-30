# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 05:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0008_auto_20160611_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libitem',
            name='date_acquired',
            field=models.DateField(default=datetime.date(2016, 6, 18)),
        ),
        migrations.AlterField(
            model_name='libitem',
            name='duedate',
            field=models.DateField(default=datetime.date(2016, 7, 9), null=True),
        ),
    ]
