from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('maps', TemplateView.as_view(template_name="maps/map.html"), name = "maps"),
]