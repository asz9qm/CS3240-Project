import datetime
from django.db import models
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your models here.


class Request(models.Model):
    subject = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    specific = models.TextField()
    def __str__(self):
        return self.subject
    def get_absolute_url(self): 
        return reverse('main:maps')

