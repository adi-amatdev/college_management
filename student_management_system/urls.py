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
    path('add_course',HodViews.add_course),
    #path('add_course_save',HodViews.add_course_save),
    path('add_student',HodViews.add_student),
    path('add_subject',HodViews.add_subject),
    path('manage_staff',HodViews.manage_staff),
    path('manage_student',HodViews.manage_student),
    path('manage_course',HodViews.manage_course),
    path('manage_subject',HodViews.manage_subject),
    path('edit_staff/<str:staff_id>',HodViews.edit_staff),
    path('edit_student/<str:student_id>',HodViews.edit_student),
    path('edit_subject/<str:subject_id>',HodViews.edit_subject),
    path('edit_course/<str:course_id>',HodViews.edit_course),
    
    path('staff/', StaffListView.as_view()),    #returns a list of all objects.
    path('staff/create/', CreateStaffAPIView.as_view()),  #creates a new object.
    path('staff/<int:pk>/', RetrieveStaffAPIView.as_view()), #returns a single object with the given primary key.
    path('staff/<int:pk>/update/', UpdateStaffAPIView.as_view()), #updates an existing object with the given primary key.
    path('staff/<int:pk>/delete/', DestroyStaffAPIView.as_view()), #deletes an existing object with the given primary key.
    path('staff/<int:pk>/detail', StaffDetailView.as_view()), #to retrieve a single MyModel object with primary key.

    path('course/', CourseListView.as_view()),    #returns a list of all objects.
    path('course/create/', CreateCourseAPIView.as_view()),  #creates a new object.
    path('course/<int:pk>/', RetrieveCourseAPIView.as_view()), #returns a single object with the given primary key.
    #path('course/<int:pk>/update/', UpdateCourseAPIView.as_view()), #updates an existing object with the given primary key.
    path('course/<int:pk>/delete/', DestroyCourseAPIView.as_view()), #deletes an existing object with the given primary key.
    path('course/<int:pk>/detail', CourseDetailView.as_view()), #to retrieve a single MyModel object with primary key.

    path('student/', StudentListView.as_view()),    #returns a list of all objects.
    path('student/create/', CreateStudentAPIView.as_view()),  #creates a new object.
    path('student/<int:pk>/', RetrieveStudentAPIView.as_view()), #returns a single object with the given primary key.
    path('student/<int:pk>/update/', UpdateStudentAPIView.as_view()), #updates an existing object with the given primary key.
    path('student/<int:pk>/delete/', DestroyStudentAPIView.as_view()), #deletes an existing object with the given primary key.
    path('student/<int:pk>/detail', StudentDetailView.as_view()), #to retrieve a single MyModel object with primary key.

    path('subject/', SubjectListView.as_view()),    #returns a list of all objects.
    path('subject/create/', CreateSubjectAPIView.as_view()),  #creates a new object.
    path('subject/<int:pk>/', RetrieveSubjectAPIView.as_view()), #returns a single object with the given primary key.
    path('subject/<int:pk>/update/', UpdateSubjectAPIView.as_view()), #updates an existing object with the given primary key.
    path('subject/<int:pk>/delete/', DestroySubjectAPIView.as_view()), #deletes an existing object with the given primary key.
    path('subject/<int:pk>/detail', SubjectDetailView.as_view()), #to retrieve a single MyModel object with primary key.
    
    path('add_staff_form_api', AddStaffFormAPIView.as_view(), name='add_staff_form_api'),
    path('add_student_form_api', AddStudentFormAPIView.as_view(), name='add_student_form_api'),
    path('add_course_form_api',add_course_form_api,name='add_course_form_api'),
    path('add_subject_form_api',AddSubjectFormAPIView.as_view(),name='add_subject_form_api'),
    
     path('courses/<int:course_id>/update/', update_course, name='update-course'),

    

    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
