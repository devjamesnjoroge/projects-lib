from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.create_user, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
]
