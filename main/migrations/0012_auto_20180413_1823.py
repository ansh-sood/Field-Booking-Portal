# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-13 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_calender_total_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='total_bookings',
            field=models.IntegerField(default=16),
        ),
    ]