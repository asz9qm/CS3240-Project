from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

class HomePageView(TemplateView):
    template_name = 'main/ratings.html'
