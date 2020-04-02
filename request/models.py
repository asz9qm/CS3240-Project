from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.


class Request(models.Model):
    subject = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    specific = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.author

    def get_absolute_url(self): 
        return reverse('main:maps')

