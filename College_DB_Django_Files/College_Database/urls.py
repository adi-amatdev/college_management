"""College_Database URL Configuration

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
from django.urls import re_path as url

from dataentry.api import StudentList,AadharList
from dataentry.api import AttendanceList,MarksList
from dataentry.api import FeesList,HostelList
from dataentry.api import DepartmentList
from dataentry.api import ImpInfoList,TeacherList
from dataentry.api import BacklogsList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    url(r'api/students_list/$',StudentList.as_view(),name='student_list'),
    url(r'api/attendance_list/$',AttendanceList.as_view(),name='attendance_list'),
    url(r'api/marks_list/$',MarksList.as_view(),name='marks_list'),
    url(r'api/aadhar_list/$',AadharList.as_view(),name='aadhar_list'),
    url(r'api/fees_list/$',FeesList.as_view(),name='fees_list'),
    url(r'api/department_list/$',DepartmentList.as_view(),name='department_list'),
    url(r'api/hostel_list/$',HostelList.as_view(),name='hostel_list'),
    url(r'api/imfinfo_list/$',ImpInfoList.as_view(),name='impinfo_list'),
    url(r'api/teachers_list/$',TeacherList.as_view(),name='teachers_list'),
    url(r'api/backlogs_list/$',BacklogsList.as_view(),name='backlogs_list'),
    
    
    
]
