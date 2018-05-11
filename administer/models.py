from django.contrib.auth.models import Permission, User
from django.db import models
import datetime


# Create your models here.

class RequestList(models.Model):
    username = models.CharField(max_length=50)
    sport1 = models.CharField(max_length=50, default="0")
    month1 = models.CharField(max_length=50, default="0")
    date1 = models.CharField(max_length=50, default="0")
    check_1 = models.CharField(max_length=15, default="0")
    check_2 = models.CharField(max_length=15, default="0")
    check_3 = models.CharField(max_length=15, default="0")
    check_4 = models.CharField(max_length=15, default="0")
    check_5 = models.CharField(max_length=15, default="0")
    check_6 = models.CharField(max_length=15, default="0")
    check_7 = models.CharField(max_length=15, default="0")
    check_8 = models.CharField(max_length=15, default="0")
    check_9 = models.CharField(max_length=15, default="0")
    check_10 = models.CharField(max_length=15, default="0")
    check_11 = models.CharField(max_length=15, default="0")
    check_12 = models.CharField(max_length=15, default="0")
    check_13 = models.CharField(max_length=15, default="0")
    check_14 = models.CharField(max_length=15, default="0")
    check_15 = models.CharField(max_length=15, default="0")
    check_16 = models.CharField(max_length=15, default="0")
    purpose = models.CharField(max_length=10000, default="Not Provided")
    status = models.CharField(max_length=15, default="None")
    date2 = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.username


# class Notifications(models.Model):

