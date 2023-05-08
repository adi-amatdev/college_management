from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from student_management_app.models import *


  
def student_home(request):
    return render(request,"student_template/student_home_template.html")


def student_view_attendance(request):
   # student=Students.objects.get(admin=request.user.id)
    #course=student.course_id
    #subjects=Subjects.objects.filter(course_id=course)
    return render(request,"student_template/student_view_attendance.html")#,{"subjects":subjects}


def student_view_attendance_post(request):
    '''subject_id=request.POST.get("subject")
    start_date=request.POST.get("start_date")
    end_date=request.POST.get("end_date")
    
    
    start_data_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_data_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Subjects.objects.get(id=subject_id)
    user_object=CustomUser.objects.get(id=request.user.id)
    stud_obj=Students.objects.get(admin=user_object)

    attendance=Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),subject_id=subject_obj)
    attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)'''
    return render(request,"student_template/student_attendance_data.html") #,{"attendance_reports":attendance_reports}


def student_apply_leave(request):
    student_obj = Students.objects.get(admin=request.user.id)
    leave_obj=LeaveReportStudent.objects.filter(student_id=student_obj)
    return render(request,"student_template/student_apply_leave.html" ,{"leave_obj":leave_obj})


def student_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_apply_leave"))
    else:
        leave_date = request.POST.get("leave_date")
        leave_msg = request.POST.get("leave_msg")
        student_obj = Students.objects.get(admin=request.user.id)
        try:
            leave_report = LeaveReportStudent(student_id=student_obj.id, leave_date=leave_date, leave_message=leave_msg, leave_status=0)
            leave_report.save()
            messages.success(request, "SUCCESSFULY SENT LEAVE APPLICATION!")
        except Exception as e:
            messages.error(request, f"FAILED TO SEND LEAVE APPLICATION! - {str(e)}")
        return HttpResponseRedirect(reverse("student_apply_leave"))


def student_feedback(request):
    student_obj=Students.objects.get(admin=request.user.id)
    feedback_obj=FeedbackStudent.objects.filter(student_id=student_obj)
    return render(request,"student_template/student_feedback.html" , {"feedback_obj":feedback_obj})

def student_send_feedback_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_feedback"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        student_obj=Students.objects.get(admin=request.user.id)
        try:
            feedback=FeedbackStudent(student_id=student_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "FEEDBACK SENT SUCCESSFULY")
            return HttpResponseRedirect(reverse("student_feedback"))
        except Exception as e:
            messages.error(request, "FAILED TO SEND FEEDBACK - " , str(e) )
            return HttpResponseRedirect(reverse("student_feedback"))
        
        
def student_profile(request):
    #user=CustomUser.objects.get(id=request.user.id)
    #student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html") #,{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))        