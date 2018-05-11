# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('check_1', models.BooleanField(default=False)),
                ('check_2', models.BooleanField(default=False)),
                ('check_3', models.BooleanField(default=False)),
                ('check_4', models.BooleanField(default=False)),
                ('check_5', models.BooleanField(default=False)),
                ('check_6', models.BooleanField(default=False)),
                ('check_7', models.BooleanField(default=False)),
                ('check_8', models.BooleanField(default=False)),
                ('check_9', models.BooleanField(default=False)),
                ('check_10', models.BooleanField(default=False)),
                ('check_11', models.BooleanField(default=False)),
                ('check_12', models.BooleanField(default=False)),
                ('check_13', models.BooleanField(default=False)),
                ('check_14', models.BooleanField(default=False)),
                ('check_15', models.BooleanField(default=False)),
                ('check_16', models.BooleanField(default=False)),
            ],
        ),
    ]