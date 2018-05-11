from django import forms
from django.contrib.auth.models import User
from .models import Calender
from django.db import models


class QueryForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = ['sport', 'month']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Calender

        fields = ['check_1', 'check_2', 'check_3', 'check_4', 'check_5', 'check_6', 'check_7', 'check_8', 'check_9',
                  'check_10', 'check_11', 'check_12', 'check_13', 'check_14', 'check_15', 'check_16', 'purpose']

