from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup', views.handleSignUp,name='handleSignUp'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('log',views.handeLogin,name='handeLogin'),
    path('logout',views.handelLogout,name='handelLogout'),
    path('profile',views.profile,name='profile'),
]
