from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'request'

urlpatterns = [
    path('', views.get_Request, name='get_Request'),
    path('list/', views.request_list, name = 'RequestList' ),
    path('allrequests/', views.all_requests, name='Requests'),
]