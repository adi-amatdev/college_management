import json
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from student_management_app import serializers
from student_management_app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . serializers import *
from student_management_app.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib import messages
from django.http import HttpRequest
from .models import Staff, StaffLeave

@login_required
def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")



@login_required
@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    session_year=request.POST.get("session_year")
    
    subject=Subjects.objects.get(id=subject_id)
    session_model=SessionYearModel.object.get(id=session_year)
    students=Students.objects.filter(course_id=subject.course_id,session_year_id=session_model)
    student_data=serializers.serialize('python',students)
    list_data=[]
    for student in student_data:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)


@login_required
def update_attendance(request):
    subjects = Subjects.objects.all()
    session_years = SessionYearModel.objects.all()
    return render(request,'staff_template/staff_update_attendance.html',{"subjects":subjects,"session_year":session_years})

@login_required
def staff_apply_leave_save(request: HttpRequest):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("staff_apply_leave"))
    else:
        leave_date = request.POST.get("leave_date")
        leave_msg = request.POST.get("leave_message")
        print(f"request.user.id: {request.user.id}")
        staff_obj = get_object_or_404(Staff, admin=request.user.id)
        print(f"staff_obj: {staff_obj}")
        try:
            leave_report = StaffLeave(
                staff_id=staff_obj,
                leave_date=leave_date,
                leave_message=leave_msg,
                leave_status=0,
            )
            leave_report.save()
            messages.success(request, "LEAVE APPLICATION SENT")
            return HttpResponseRedirect(reverse("staff_apply_leave"))
        except Exception as e:
            messages.error(request, f"LEAVE APPLICATION FAILED - {str(e)}")
            return HttpResponseRedirect(reverse("staff_apply_leave"))
     
@login_required   
def staff_send_feedback_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("staff_feedback"))
    else:
        feedback_msg = request.POST.get("feedback_msg")
        print(f"request.user.id: {request.user.id}")
        staff_obj = get_object_or_404(Staff, admin=request.user.id)
        print(f"staff_obj: {staff_obj}")
        try:
            feedback = FeedbackStaff(
                staff_id=staff_obj,
                feedback=feedback_msg,
                feedback_reply=""  
            )
            feedback.save()
            messages.success(request, "FEEDBACK SUCCESSFULY SENT!")
            return HttpResponseRedirect(reverse("staff_feedback"))
        except Exception as e:
            messages.error(request, f"FAILED TO SEND FEEDBACK - {str(e)}")
            return HttpResponseRedirect(reverse("staff_feedback"))
    

@login_required
def staff_apply_leave(request):
    staff_obj = Staff.objects.get(admin=request.user.id)
    leave_data = StaffLeave.objects.filter(staff_id=staff_obj)
    return render(request,"staff_template/staff_apply_leave.html",{"leave_data":leave_data})
  
@login_required   
def staff_feedback(request):
    staff_obj = Staff.objects.get(admin=request.user.id)
    feedback_obj = FeedbackStaff.objects.filter(staff_id=staff_obj)
    return render(request,"staff_template/staff_feedback.html",{"feedback_obj":feedback_obj})


def staff_view_test_details(request):
    subjects = Subjects.objects.all()
    tests = TestDetails.objects.all()
    return render(request,"staff_template/view_test_details.html",{"tests":tests, "subjects":subjects})

    
@login_required
def staff_edit_result(request):
    #subjects = Subjects.objects.all()
    #session_years = SessionYearModel.objects.all()
    return render(request,"staff_template/edit_student_result.html")

@login_required
def staff_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    staff=Staff.objects.get(admin=user)
    return render(request,"staff_template/staff_profile.html",{"user":user,"staff":staff})

@login_required
def staff_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_profile"))
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

            staff=Staff.objects.get(admin=customuser)
            staff.address=address
            staff.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("staff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("staff_profile"))   

@login_required
def staff_edit_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    staff=Staff.objects.get(admin=user)
    return render(request,"staff_template/staff_edit_profile.html",{"user":user,"staff":staff})      

from django.db import transaction
#import xlrd
from django.shortcuts import get_object_or_404
import time

def excel_dump_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        
        try:
            with transaction.atomic():
                # Read the Excel file into a pandas DataFrame
                df = pd.read_excel(file, sheet_name='Sheet1')

                # Iterate over the rows of the DataFrame and create TestScores objects
                for index, row in df.iterrows():
                    subject_code = row['subject_code']
                    subjects = get_object_or_404(Subjects, subject_code=subject_code)
                    username = row['usn']
                    usernames = get_object_or_404(CustomUser, username=username)

                    testscore = TestScores(
                        subject_code=subjects,
                        usn=usernames,
                        test1=row['test1'],
                        test2=row['test2'],
                        test3=row['test3'],
                        final=row['final'],
                        attendance=row['attendance']
                    )
                    testscore.save()

            time.sleep(1)
            messages.success(request, "ADDED TEST SCORES!")
            return HttpResponseRedirect("/add_results")
            
        
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD TEST SCORES - " + str(e))
            return HttpResponseRedirect("/add_results")    
    
    else:
        return render(request, "staff_template/add_results_template.html")

@login_required
def add_results(request):
    subjects = Subjects.objects.all()
    return render(request,"staff_template/add_results_template.html",{"subjects":subjects})

@login_required
def add_testdetails_form_save(request):
    if request.method != "POST":
        return HttpResponse("METHOD NOT ALLOWED")
    else:
        subject_code = request.POST.get("subject_code")
        semester = request.POST.get("semester")
        test1_date = request.POST.get("test1_date")
        test2_date = request.POST.get("test2_date")
        test3_date = request.POST.get("test3_date")
        
        try:
            with transaction.atomic():
                subject = Subjects.objects.get(subject_code=subject_code)  # Fetch the Subjects instance
                testdetails = TestDetails.objects.create(
                    subject_code=subject,  # Assign the Subjects instance
                    semester=semester,
                    test1_date=test1_date,
                    test2_date=test2_date,
                    test3_date=test3_date,
                )
                messages.success(request, "ADDED TEST DETAILS!")
                return HttpResponseRedirect("/add_results")
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD TEST DETAILS - " + str(e))
            return HttpResponseRedirect("/add_results")
        
@login_required
def edit_testdetails_form(request):
    test = TestDetails.objects.all()
    return render(request,"staff_template/edit_testdetails.html" ,{"test":test})
        
def edit_testdetails(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        testdetails_id = request.POST.get('testdetails_id')
        semester = request.POST.get("semester")
        test1_date = request.POST.get("test1_date")
        test2_date = request.POST.get("test2_date")
        test3_date = request.POST.get("test3_date")
        
        try:
            testdetails = TestDetails.objects.get(id=testdetails_id)
            testdetails.semester = semester
            testdetails.test1_date = test1_date
            testdetails.test2_date = test2_date
            testdetails.test3_date = test3_date
            testdetails.save()
            
            messages.success(request, "SUCCESSFULLY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_testdetails_form/" + testdetails_id)
        
        except Exception as e:
            messages.error(request, "FAILED TO UPDATE THE DETAILS - " + str(e))
            return HttpResponseRedirect("/edit_testdetails_form/" + testdetails_id)   
        
    
