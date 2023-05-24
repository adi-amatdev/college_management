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
    path('manage_admin',HodViews.manage_admin),
    path('manage_course',HodViews.manage_course),
    
    path('delete_course',HodViews.delete_course, name='delete_course'),
    path('delete_course_confirm/<str:course_id>/',delete_course_confirm, name='delete_course_confirm'),
    path('hod_profile', HodViews.hod_profile, name="hod_profile"),
    path('edit_hod_profile_form', HodViews.edit_hod_profile_form, name="edit_hod_profile_form"),
    path('hod_edit_profile', HodViews.hod_edit_profile, name="hod_edit_profile"), 

    path('delete_staff', HodViews.delete_staff, name="delete_staff"), 
    path('delete_staff_confirm/<str:staff_id>', HodViews.delete_staff_confirm, name="delete_staff_confirm"),
    path('delete_student', HodViews.delete_student, name="delete_student"),
    path('delete_student_confirm/<str:student_id>', HodViews.delete_student_confirm, name="delete_student_confirm"),
    path('delete_subject', HodViews.delete_subject, name="delete_subject"),
    path('delete_subject_confirm/<str:subject_id>', HodViews.delete_subject_confirm, name="delete_subject_confirm"),
    path('delete_session', HodViews.delete_session, name="delete_session"),
    path('delete_session_confirm/<str:session_id>', HodViews.delete_session_confirm, name="delete_session_confirm"),
    path('delete_admin', HodViews.delete_admin_hod, name="delete_admin_hod"),
    path('delete_admin_confirm/<str:admin_id>', HodViews.delete_admin_hod_confirm, name="delete_admin_hod_confirm"),
     
    
    path('edit_subject/<str:subject_id>',HodViews.edit_subject),
    path('edit_course/<str:course_id>',HodViews.edit_course),
    path('add_session',HodViews.add_session),
    path('manage_session',HodViews.manage_session),

    path('staff_home',StaffViews.staff_profile,name='staff_profile'),
    path('get_students',StaffViews.get_students, name="get_students"),
    path('staff_view_test_details',StaffViews.staff_view_test_details,name="staff_view_test_details"),
    path('edit_student_result', StaffViews.staff_edit_result, name="staff_edit_result"),
    
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

    path('student_view_results',StudentViews.student_view_results,name = 'student_view_results'),
   
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_send_feedback_save', StudentViews.student_send_feedback_save, name="student_send_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_edit_profile', StudentViews.student_edit_profile, name="student_edit_profile"),
    path('student_edit_profile_save', StudentViews.edit_student_profile_save, name="edit_student_profile_save"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path("cie_schedule",StudentViews.cie_schedule,name="cie_schedule"),

    
    
    #working related urls 
    path('add_student_form_save',HodViews.add_student_form_save,name='add_student_form_save'),
    path('add_staff_form_save',HodViews.add_staff_form_save,name='add_staff_form_save'),
    path('add_admin_form_save',HodViews.add_admin_form_save,name='add_admin_form_save'),
    path('add_course_form_api',add_course_form_api,name='add_course_form_api'),
    path('add_subject_form_save',HodViews.add_subject_form_save,name='add_subject_form_save'),
    path('add_session_form_api', add_session_form_api, name='add_session_form_api'),
    
    
    path('courses/<int:course_id>/update/', update_course, name='update-course'),
    path('edittestdetails/<int:testdetails_id>/update/', StaffViews.edit_testdetails, name='edit_testdetails'),
    path('edit_testdetails_form',StaffViews.edit_testdetails_form,name='edit_testdetails_form'),
    
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
    
    path('manage_subject',HodViews.manage_subject,name='manage_subject'),
    path("get_subjects_list",HodViews.get_subjects_list,name="get_subjects_list"),
    
    path('manage_students',HodViews.manage_students,name='manage_students'),
    path("get_students_list",HodViews.get_students_list,name="get_students_list"),
    
    path('manage_staff',HodViews.manage_staff,name='manage_staff'),
    path("get_staff_list",HodViews.get_staff_list,name="get_staff_list"),

    path('edit_testdetails/<int:testdetails_id>/', StaffViews.edit_testdetails, name='edit_testdetails'),
    path('add_testdetails_form_save',StaffViews.add_testdetails_form_save,name='add_testdetails_form_save'),
    path('excel_dump_view', StaffViews.excel_dump_view, name='excel_dump_view'),
    path('add_results',StaffViews.add_results,name="add_results"),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
