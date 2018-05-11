from django import forms
from django.contrib.auth.models import User
from .models import RequestList
from django.db import models


class RequestListForm(forms.ModelForm):
    class Meta:
        model = RequestList
        fields = ['sport1']
