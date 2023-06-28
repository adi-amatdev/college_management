import json
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from student_management_app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student_management_app.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib import messages
from django.http import HttpRequest
from .models import Staff, StaffLeave
from django.db import transaction
from django.shortcuts import get_object_or_404
import time


@login_required
def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

    
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


@login_required
def get_test_details(request):
    departments = Courses.objects.all()
    return render(request,"staff_template/get_test_details_template.html",{"departments":departments})


def staff_view_test_details(request):
    department = request.POST.get('department')
    semester = request.POST.get('semester')
    tests = TestDetails.objects.filter(subject_code__course_id__course_name=department, semester=semester)
    return render(request, "staff_template/view_test_details.html", {"tests": tests})


@login_required
def add_results(request):
    subjects = Subjects.objects.all()
    return render(request,"staff_template/add_results_template.html",{"subjects":subjects})

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
def filter_for_edit_results(request):
    departments = Courses.objects.all()
    subcodes = Subjects.objects.all()
    return render(request,"staff_template/filter_for_edit_results.html",{"departments":departments,"subcodes":subcodes})
   
    
@login_required
def staff_manage_testscore(request):
    department = request.POST.get('department')
    subjectcode = request.POST.get('subject_code')
    tests = TestScores.objects.filter(subject_code__course_id__course_name=department,subject_code=subjectcode)
    return render(request,"staff_template/staff_manage_testscore.html",{"tests":tests})
    
    
@login_required
def edit_testdetails_form(request):
    test = TestDetails.objects.all()
    return render(request,"staff_template/edit_testdetails.html" ,{"test":test})


@login_required
def edit_testdetails(request, testdetails_id):
    testdetails = get_object_or_404(TestDetails, id=testdetails_id)

    if request.method == 'POST':
        subject_code = request.POST.get("subject_code")
        semester = request.POST.get("semester")
        test1_date = request.POST.get("test1_date")
        test2_date = request.POST.get("test2_date")
        test3_date = request.POST.get("test3_date")

        try:
            subject = get_object_or_404(Subjects, subject_code=subject_code)
            testdetails.subject_code = subject
            testdetails.semester = semester
            testdetails.test1_date = test1_date
            testdetails.test2_date = test2_date
            testdetails.test3_date = test3_date
            testdetails.save()

            messages.success(request, "SUCCESSFULLY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_testdetails/" + str(testdetails_id))

        except Exception as e:
            messages.error(request, "FAILED TO UPDATE THE DETAILS - " + str(e))
            return HttpResponseRedirect("/edit_testdetails/" + str(testdetails_id))

    else:
        return render(request, "staff_template/edit_testdetails.html", {"testdetails": testdetails})
    
    
@login_required
def edit_testscores_form(request):
    test = TestScores.objects.all()
    return render(request,"staff_template/edit_testscores.html" ,{"test":test})


@login_required
def edit_testscores(request, testscores_id):
    testscores = get_object_or_404(TestScores, id=testscores_id)
    
    if request.method == 'POST':
        test1_scores = request.POST.get("test1")
        test2_scores = request.POST.get("test2")
        test3_scores = request.POST.get("test3")
        attendance = request.POST.get("attendance")

        try:
            testscores.test1 = test1_scores
            testscores.test2 = test2_scores
            testscores.test3 = test3_scores
            testscores.attendance = attendance
            testscores.save()

            messages.success(request, "SUCCESSFULLY UPDATED SCORES")
            return HttpResponseRedirect("/edit_testscores/" + str(testscores_id))

        except Exception as e:
            messages.error(request, "FAILED TO UPDATE THE SCORES - " + str(e))
            return HttpResponseRedirect("/edit_testscores/" + str(testscores_id))

    else:
        return render(request, "staff_template/edit_testscores.html", {"testscores": testscores})


@login_required
def staff_apply_leave(request):
    staff_obj = Staff.objects.get(admin=request.user.id)
    leave_data = StaffLeave.objects.filter(staff_id=staff_obj)
    return render(request,"staff_template/staff_apply_leave.html",{"leave_data":leave_data})

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
def staff_feedback(request):
    staff_obj = Staff.objects.get(admin=request.user.id)
    feedback_obj = FeedbackStaff.objects.filter(staff_id=staff_obj)
    return render(request,"staff_template/staff_feedback.html",{"feedback_obj":feedback_obj})


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
    

def delete_test_details(request): 
    testdetails_id = request.POST.get('testdetails_id')
    try:
    # Retrieve the TestDetails object
        test_details = TestDetails.objects.get(id=testdetails_id)
    # Delete the TestDetails object
        test_details.delete()
        messages.success(request,"SUCCESSFULY DELETED THE DETAILS")
        return render(request,"staff_template/delete_testdetails.html",{"testdetails":test_details}) 
    except Exception as e:
        messages.error(request,"FAILED TO DELETE THE DETAILS " +str(e))
        return HttpResponseRedirect("/delete_test_details_confirm/"+str(testdetails_id))
    

def delete_test_details_confirm(request, testdetails_id):
    print(testdetails_id)
    try:
        test_details = TestDetails.objects.get(id=testdetails_id)
        return render(request, "staff_template/delete_testdetails.html", {"testdetails": test_details})
    except TestDetails.DoesNotExist:
        messages.error(request, "Test Details does not exist")
        return render(request, "staff_template/delete_testdetails.html", {"testdetails": None})


        
    
