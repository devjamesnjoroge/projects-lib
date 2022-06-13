from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.create_user, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    path('profile/', views.create_profile, name='profile'),
    path('profile/display/<uname>', views.profile_display, name='profile_display'),
]
