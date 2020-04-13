from django.urls import path
from . import views
from . views import RequestListView, RequestDeleteView, RequestDetailView, RequestListHistoryView
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'request'

urlpatterns = [
    path('new/', views.get_Request, name='request-new'),
    path('history/', RequestListHistoryView.as_view(), name = 'request-list-history' ),
    path('', RequestListView.as_view() , name='request-list'),
    path('history/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),
    path('history/<int:pk>/delete/', RequestDeleteView.as_view() , name='request-delete'),
]
