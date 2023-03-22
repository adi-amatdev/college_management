"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from student_management_app import views, HodViews
from django.conf.urls.static import static 
from student_management_system import settings
from student_management_app.HodViews import *

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Staff',CreateStaffAPIView )
router.register('Staff',RetrieveStaffAPIView)
router.register('Staff',UpdateStaffAPIView )
router.register('Staff', DestroyStaffAPIView)
router.register('Staff',DestroyStaffAPIView)
router.register('Staff',StaffDetailView)


urlpatterns = [
    path('demo',views.showdemopage),
    path('admin/', admin.site.urls),
    
    
    path('',views.showloginpage),
    path('get_user_details',views.getuserdetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin),
    path('admin_home',HodViews.admin_home),
    path('add_staff',HodViews.add_staff),
    #path('add_staff_save',HodViews.add_staff_save)
    
    path('staff/', StaffListView.as_view()),    #returns a list of all objects.
    path('staff/create/', CreateStaffAPIView.as_view()),  #creates a new object.
    path('staff/<int:pk>/', RetrieveStaffAPIView.as_view()), #returns a single object with the given primary key.
    path('staff/<int:pk>/update/', UpdateStaffAPIView.as_view()), #updates an existing object with the given primary key.
    path('staff/<int:pk>/delete/', DestroyStaffAPIView.as_view()), #deletes an existing object with the given primary key.
    path('staff/<int:pk>/detail', StaffDetailView.as_view()), #to retrieve a single MyModel object with primary key.
    
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
