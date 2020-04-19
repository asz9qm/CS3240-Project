from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

LOC_CHOICES = (
    ('Alderman Library', 'Alderman Library'),
    ('Clark Hall','Clark Hall'),
    ('Clemons Library','Clemons Library'),
    ('Rice Hall','Rice Hall'),
    ('Thorton Stacks','Thorton Stacks'),
)


SUBJECTS = (
    ('Accounting & Finance','Accounting & Finance'),
    ('Architecture', 'Architecture'),
    ('Arts & Humanities','Arts & Humanities'),
    ('Biological Science','Biological Science'),
    ('Chemical Engineering','Chemical Engineering'),
    ('Chemistry','Chemistry'),
    ('Computer Sience & Information Systems','Computer Sience & Information Systems'),
    ('Economics','Economics'),
    ('Electrical Engineering','Electrical Engineering'),
    ('Environmental Science','Environmental Science'),
    ('Geography','Geography'),
    ('History','History'),
    ('Law','Law'),
    ('Material Science','Material Science'),
    ('Mathematics','Mathematics'),
    ('Medecine','Medecine'),
    ('Modern Languages','Modern Languages'),
    ('Nursing','Nursing'),
    ('Philosophy','Philosophy'),
    ('Physics','Physics'),
    ('Psychology','Psychology'),
    ('Religion','Religion'),
    ('Sociology','Sociology'),
    ('Other','Other'),   
)


class Request(models.Model):
    subject = models.CharField(max_length=50, choices=SUBJECTS)
    location = models.CharField(max_length=1000, choices=LOC_CHOICES)
    specific = models.TextField(max_length=1000, default='')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.author.username

    def get_absolute_url(self): 
        return reverse('main:maps')

