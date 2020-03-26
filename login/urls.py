from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'login'

urlpatterns = [
    path('', TemplateView.as_view(template_name="login/index.html"), name="display_login"),
    path('profile/', views.make_profile, name="make_profile"),
    path('info/', views.display_profile, name="display_profile"),
    path('update/', views.update_profile, name="update_profile"),
    path('login/', include('allauth.urls')),
]