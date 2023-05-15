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
from django.urls import path
from student_management_app import views, HodViews,StaffViews,StudentViews
from django.conf.urls.static import static 
from student_management_system import settings
from student_management_app.HodViews import *
from student_management_app.StaffViews import *
from student_management_app.StudentViews import *

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Staff',CreateStaffAPIView )
router.register('Staff',RetrieveStaffAPIView)
router.register('Staff',UpdateStaffAPIView )
router.register('Staff', DestroyStaffAPIView)
router.register('Staff',DestroyStaffAPIView)
router.register('Staff',StaffDetailView)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('',views.showloginpage,name='show_login'),
    path('get_user_details',views.getuserdetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin,name='do_login'),
    path('admin_home',HodViews.hod_profile,name='hod_profile'),
    path('student_home',StudentViews.student_profile,name='student_profile'),
    path('add_admin',HodViews.add_admin),
    path('add_staff',HodViews.add_staff),
    path('add_course',HodViews.add_course),
    path('add_student',HodViews.add_student),
    path('add_subject',HodViews.add_subject),
    path('manage_staff',HodViews.manage_staff),
    path('manage_admin',HodViews.manage_admin),
    path('manage_student',HodViews.manage_student),
    path('manage_course',HodViews.manage_course),
    path('manage_subject',HodViews.manage_subject),
    path('delete_course/<str:course_id>/',delete_course_save, name='delete_course_save'),
    path('hod_profile', HodViews.hod_profile, name="hod_profile"),
    path('edit_hod_profile_form', HodViews.edit_hod_profile_form, name="edit_hod_profile_form"),
    path('hod_edit_profile', HodViews.hod_edit_profile, name="hod_edit_profile"), 
     
    
    path('edit_subject/<str:subject_id>',HodViews.edit_subject),
    path('edit_course/<str:course_id>',HodViews.edit_course),
    path('add_session',HodViews.add_session),
    path('manage_session',HodViews.manage_session),

    path('staff_home',StaffViews.staff_profile,name='staff_profile'),
    path('staff_take_attendance',StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students',StaffViews.get_students, name="get_students"),
    path('save_attendance_data',StaffViews.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance',StaffViews.update_attendance,name="staff_update_attendance"),
    path('get_attendance_data',StaffViews.save_attendance_data,name='save_attendance_data'), 
    path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
    path('edit_student_result', StaffViews.staff_edit_result, name="staff_edit_result"),

    
    path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
    
    
    path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_send_feedback_save',StaffViews.staff_send_feedback_save,name="staff_send_feedback_save"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
    path('staff_edit_profile', StaffViews.staff_edit_profile, name="staff_edit_profile"),
    
    path("replyto_staff_feedback",HodViews.replyto_staff_feedback,name="replyto_staff_feedback"),
    path("replyto_student_feedback",HodViews.replyto_student_feedback,name="replyto_student_feedback"),
     
    path('student_feedback_reply_msg',HodViews.student_feedback_reply_msg,name="student_feedback_reply_msg"),
    path('staff_feedback_reply_msg',HodViews.staff_feedback_reply_msg,name="staff_feedback_reply_msg"),

    path('student_view_attendance',StudentViews.student_view_attendance,name = 'student_view_attendance'),
    path('student_view_attendance_post',StudentViews.student_view_attendance_post,name = 'student_view_attendance_post'),
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_send_feedback_save', StudentViews.student_send_feedback_save, name="student_send_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_edit_profile', StudentViews.student_edit_profile, name="student_edit_profile"),
    path('student_edit_profile_save', StudentViews.edit_student_profile_save, name="edit_student_profile_save"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),

    
    
    #working related urls 
    path('add_student_form_save',HodViews.add_student_form_save,name='add_student_form_save'),
    path('add_staff_form_save',HodViews.add_staff_form_save,name='add_staff_form_save'),
    path('add_admin_form_save',HodViews.add_admin_form_save,name='add_admin_form_save'),
    path('add_course_form_api',add_course_form_api,name='add_course_form_api'),
    path('add_subject_form_save',HodViews.add_subject_form_save,name='add_subject_form_save'),
    path('add_session_form_api', add_session_form_api, name='add_session_form_api'),
    
    path('courses/<int:course_id>/update/', update_course, name='update-course'),
    
    path('edit_admin/<str:admin_id>',HodViews.edit_admin,name='edit_admin'),
    path('edit_staff/<str:staff_id>',HodViews.edit_staff),
    path('edit_student/<str:student_id>',HodViews.edit_student),
    path('edit_admin_save',HodViews.edit_admin_form,name='edit_admin_save'),
    path('edit_staff_save',HodViews.edit_staff_form,name='edit_staff_save'),
    path('edit_student_save',HodViews.edit_student_form,name='edit_student_save'),
    path('edit_subject/<str:subject_id>',HodViews.edit_subject),
    path('edit_subject_save',HodViews.edit_subject_form,name='edit_subject_save'),
    path('edit_session/<int:session_year_id>/', HodViews.edit_session, name='edit_session'),

    path("student_leave_status",HodViews.student_leave_status,name="student_leave_status"),
    path("staff_leave_status",HodViews.staff_leave_status,name="staff_leave_status"),

    path('approve_student_leave/<str:leave_id>',HodViews.approve_student_leave,name="approve_student_leave"),
    path('disapprove_student_leave/<str:leave_id>',HodViews.disapprove_student_leave,name="disapprove_student_leave"),
    path("approve_staff_leave/<str:leave_id>",HodViews.approve_staff_leave,name="approve_staff_leave"),
    path("disapprove_staff_leave/<str:leave_id>",HodViews.disapprove_staff_leave,name="disapprove_staff_leave"),

    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
