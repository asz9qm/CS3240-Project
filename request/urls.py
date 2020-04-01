from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'request'

urlpatterns = [
    path('', views.get_Request, name='get_Request'),
    path('list', views.RequestList.as_view(), name = 'RequestList' ),
    path('3/<int:pk>/', views.DetailView.as_view(), name='Requests'),
    path('accept/<int:pk>/', views.Accept.as_view(), name="accept"),
]