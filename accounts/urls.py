from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
   path('signup', views.Register, name = "signup"),
   path('signin', views.signin, name = "signin"),
   path('signout', views.signout, name = "signout"), 
   path('forget', views.ForgetPassword, name = "forget"),
   path('change-password/<token>/', views.ChangePassword, name = "change_password"),

]

 