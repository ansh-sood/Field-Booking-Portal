# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-13 11:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administer', '0006_auto_20180413_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='status',
            field=models.CharField(default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='requestlist',
            name='date2',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 13, 17, 0, 19, 543032)),
        ),
    ]
