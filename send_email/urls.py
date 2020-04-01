from . import views
from django.urls import path

app_name = 'send_email'


urlpatterns = [

	path('', views.mail, name ="email"),
]