from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

LOC_CHOICES = (
    ('Clemons Library','Clemons Library'),
    ('Alderman Library', 'Alderman Library'),
    ('Thorton Stacks','Thorton Stacks'),
    ('Rice Hall','Rice Hall'),
    ('Clark Hall','Clark Hall'),
)

class Request(models.Model):
    subject = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=1000, choices=LOC_CHOICES)
    specific = models.TextField(max_length=1000, default='')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.author.username

    def get_absolute_url(self): 
        return reverse('main:maps')

