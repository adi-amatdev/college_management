from django.contrib import admin
from django.urls import path,include 
from main import views 


urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    
    path("signup/",views.signup,name = 'signup'),
    path("signin/",views.signin,name='signin'),
    path("logout/",views.logout,name='logout'),
]