# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-12 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_calender_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='purpose',
            field=models.CharField(default='Not Provided', max_length=10),
        ),
    ]
