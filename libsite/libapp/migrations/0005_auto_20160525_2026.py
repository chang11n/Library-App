# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0004_auto_20160525_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libitem',
            name='duedate',
            field=models.DateField(default=datetime.date(2016, 5, 25), null=True),
        ),
    ]
