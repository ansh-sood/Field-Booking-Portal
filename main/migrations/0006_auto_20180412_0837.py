# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-12 03:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180411_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calender',
            name='req_user_1',
        ),
        migrations.RemoveField(
            model_name='calender',
            name='req_user_2',
        ),
        migrations.RemoveField(
            model_name='calender',
            name='req_user_3',
        ),
    ]
