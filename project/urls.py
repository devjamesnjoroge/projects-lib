from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.create_user, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    path('profile/', views.create_profile, name='profile'),
    path('profile/display/<uname>', views.profile_display, name='profile_display'),
    path('profile/edit/<uname>', views.profile_edit, name='profile_edit'),
    path('project/add/', views.add_project, name='add_project'),
    path('projects/', views.projects, name='projects'),
    path('project/details/<int:pid>', views.project_details, name='project_details'),
    path('rate/<pid>', views.rate, name='rate'),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profiles/', views.ProfileList.as_view()),
    re_path(r'^api-token-auth/', obtain_auth_token)
]
