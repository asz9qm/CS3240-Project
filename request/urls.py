from django.urls import path
from . import views
from . views import RequestListView, RequestListHistoryView
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'request'

urlpatterns = [
    path('', views.get_Request, name='get_Request'),
    path('list/', RequestListHistoryView.as_view(), name = 'RequestList' ),
    path('allrequests/', RequestListView.as_view() , name='Requests'),
]
