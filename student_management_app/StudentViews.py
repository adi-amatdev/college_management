from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from student_management_app.models import *
from django.contrib.auth.decorators import login_required


@login_required
def student_home(request):
    return render(request,"student_template/student_home_template.html")

@login_required
def student_view_attendance(request):
   # student=Students.objects.get(admin=request.user.id)
    #course=student.course_id
    #subjects=Subjects.objects.filter(course_id=course)
    return render(request,"student_template/student_view_attendance.html")#,{"subjects":subjects}

@login_required
def student_view_attendance_post(request):
    return render(request,"student_template/student_attendance_data.html") #,{"attendance_reports":attendance_reports}

@login_required
def student_apply_leave(request):
    student_obj = Students.objects.get(admin=request.user.id)
    leave_obj=StudentLeave.objects.filter(student_id=student_obj)
    return render(request,"student_template/student_apply_leave.html" ,{"leave_obj":leave_obj})

@login_required
def student_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_apply_leave"))
    else:
        leave_date = request.POST.get("leave_date")
        leave_msg = request.POST.get("leave_msg")
        student_obj = Students.objects.get(admin=request.user.id)
        try:
            leave_report = StudentLeave(student_id=student_obj.id, leave_date=leave_date, leave_message=leave_msg, leave_status=0)
            leave_report.save()
            messages.success(request, "SUCCESSFULY SENT LEAVE APPLICATION!")
        except Exception as e:
            messages.error(request, f"FAILED TO SEND LEAVE APPLICATION! - {str(e)}")
        return HttpResponseRedirect(reverse("student_apply_leave"))

@login_required
def student_feedback(request):
    student_obj=Students.objects.get(admin=request.user.id)
    feedback_obj=FeedbackStudent.objects.filter(student_id=student_obj)
    return render(request,"student_template/student_feedback.html" , {"feedback_obj":feedback_obj})

@login_required
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
        
@login_required      
def student_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html" ,{"user":user,"student":student})

@login_required
def student_edit_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_edit_profile.html",{"user":user,"student":student})

@login_required
def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        student_id = request.POST.get('student_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')
        father_name = request.POST.get('father_name')
        father_num =  request.POST.get('father_num')
        mother_name = request.POST.get('mother_name')
        mother_num = request.POST.get('mother_num')
        gaurdian_name= request.POST.get('gaurdian_name')
        gaurdian_num = request.POST.get('gaurdian_num')
        parent_or_gaurdian_email = request.POST.get('parent_or_gaurdian_email')
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.email=email
            student.username=username
            student.course=course
            student.gender=gender
            student.session_start_year=session_start_year
            student.session_end_year=session_end_year
            student.father_name=father_name
            student.father_num=father_num
            student.mother_name=mother_name
            student.mother_num=mother_num
            student.gaurdian_name=gaurdian_name
            student.gaurdian_num=gaurdian_num
            student.parent_or_gaurdian_email=parent_or_gaurdian_email
            
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except Exception as e:
            messages.error(request,"FAILED TO UPDATE THE DETAILS "+str(e))
            return HttpResponseRedirect("/edit_student/"+student_id)      

@login_required
def edit_student_profile_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get("address")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')
        father_name = request.POST.get('father_name')
        father_num =  request.POST.get('father_num')
        mother_name = request.POST.get('mother_name')
        mother_num = request.POST.get('mother_num')
        gaurdian_name= request.POST.get('gaurdian_name')
        gaurdian_num = request.POST.get('gaurdian_num')
        parent_or_gaurdian_email = request.POST.get('parent_or_gaurdian_email')
            
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()
            
            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            student_model.course = course
            student_model.gender = gender
            student_model.session_start_year = session_start_year
            student_model.session_end_year = session_end_year
            student_model.father_name = father_name
            student_model.father_num = father_num
            student_model.mother_name = mother_name
            student_model.mother_num = mother_num
            student_model.gaurdian_name = gaurdian_name
            student_model.gaurdian_num = gaurdian_num
            student_model.parent_or_gaurdian_email = parent_or_gaurdian_email
            
            student_model.save()
            
            messages.success(request,"SUCCESSFULY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except Exception as e:
            messages.error(request,"FAILED TO UPDATE THE DETAILS "+str(e))
            return HttpResponseRedirect("/edit_student/"+student_id)  