from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from user_auth import views

app_name = 'user_auth'

urlpatterns = [
    path('base/', views.home, name='base'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
