from django.contrib.auth.models import Permission, User
from django.db import models
import datetime


# Create your models here.

class Calender(models.Model):
    sport = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
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
    total_bookings = models.IntegerField(default=16)

    def __str__(self):
        return self.sport + ' - ' + self.month
