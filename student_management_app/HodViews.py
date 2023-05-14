from urllib import request
from django.contrib import messages
from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from student_management_app.models import CustomUser, Staff
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt


 
@login_required
def admin_home(request):
    return render(request,"hod_template/home_content.html")


def add_admin(request):
    courses = Courses.objects.all()
    return render(request,"hod_template/add_admin_template.html",{"courses":courses})

def add_staff(request):
    courses = Courses.objects.all()
    return render(request,"hod_template/add_staff_template.html",{"courses":courses})


def add_staff_form_save(request):
    if request.method != "POST":
        return HttpResponse("METHOD NOT ALLOWED")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        gender = request.POST.get('gender')
        email = request.POST.get("email")
        password = request.POST.get("password")
        department_id = request.POST.get("department_id")
        address = request.POST.get("address")
        try:
            with transaction.atomic():
                user = CustomUser.objects.create_user(
                    password=password,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    user_type=2,
                )
                staff = Staff.objects.create(admin=user, address=address,gender=gender,department_id=department_id)
                messages.success(request, "ADDED STAFF DETAILS!")
                return HttpResponseRedirect("/add_staff")
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD STAFF DETAILS - " + str(e))
            return HttpResponseRedirect("/add_staff")
        

def add_admin_form_save(request):
    if request.method != "POST":
        return HttpResponse("METHOD NOT ALLOWED")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        gender = request.POST.get('gender')
        email = request.POST.get("email")
        password = request.POST.get("password")
        department_id = request.POST.get("department_id")
        address = request.POST.get("address")
        try:
            with transaction.atomic():
                user = CustomUser.objects.create_user(
                    password=password,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    user_type=1,
                    is_superuser = 1,
                )
                admin = AdminHOD.objects.create(admin=user, address=address,gender=gender,department_id=department_id)
                messages.success(request, "ADDED ADMIN DETAILS!")
                return HttpResponseRedirect("/add_admin")
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD ADMIN DETAILS - " + str(e))
            return HttpResponseRedirect("/add_admin")


def add_course(request):
    return render(request,"hod_template/add_course_template.html")

class CreateCourseAPIView(CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()


def add_student(request): 
    courses = Courses.objects.all()
    session_years = SessionYearModel.objects.all()
    return render(request,"hod_template/add_student_template.html",{"courses":courses, "session_years":session_years})

@login_required(login_url='login')
def add_student_form_save(request):
    if request.method != 'POST':
        return HttpResponse("METHOD NOT ALLOWED")

    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    address = request.POST.get('address')
    course_id = request.POST.get('course_id')
    session_year_id_id = request.POST.get('session_year_id_id')
    section = request.POST.get('section')
    gender = request.POST.get('gender')
    father_name = request.POST.get('father_name')
    father_num =  request.POST.get('father_num')
    mother_name = request.POST.get('mother_name')
    mother_num = request.POST.get('mother_num')
    gaurdian_name= request.POST.get('gaurdian_name')
    gaurdian_num = request.POST.get('gaurdian_num')
    parent_or_gaurdian_email = request.POST.get('parent_or_gaurdian_email')
    # Create a new user
    try:
        user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username,user_type=3)
        user.save()
    except Exception as e:
        messages.error(request, "FAILED TO ADD STUDENT - " + str(e))
        return redirect('/add_student')
    # Create a new student
    try:
        student = Students.objects.create(admin=user, gender=gender, section=section, address=address, course_id_id=course_id, session_year_id_id=session_year_id_id,father_name=father_name,father_num=father_num,mother_name=mother_name,mother_num=mother_num,gaurdian_name=gaurdian_name,gaurdian_num=gaurdian_num,parent_or_gaurdian_email=parent_or_gaurdian_email)
        student.save()
        messages.success(request, "ADDED STUDENT DETAILS!")
    except Exception as e:
        user.delete()  # Delete the user created above
        messages.error(request, "FAILED TO ADD STUDENT - " + str(e))
        return redirect('/add_student')

    return redirect('/add_student')



def add_subject(request):
    courses = Courses.objects.all()
    #staffs = CustomUser.objects.filter(user_type=2)
    staffs = CustomUser.objects.all()
    return render(request,"hod_template/add_subject_template.html",{"staffs":staffs, "courses":courses})

def manage_admin(request):
    admins = AdminHOD.objects.all()
    return render(request,"hod_template/manage_admin_template.html",{ "admins":admins})  

def manage_staff(request):
    staffs = Staff.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{ "staffs":staffs})

def manage_student(request):
    students = Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{ "students":students})

def manage_course(request):
    courses = Courses.objects.all()
    return render(request,"hod_template/manage_course_template.html",{ "courses":courses})

def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request,"hod_template/manage_subject_template.html",{ "subjects":subjects})
    
@api_view(['POST'])
def add_course_form_api(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
def add_subject_form_save(request):
    if request.method != "POST":
        return HttpResponse("METHOD NOT ALLOWED")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        staff_id = request.POST.get("staff_id")
        subject_code = request.POST.get("subject_code")
        try:
            with transaction.atomic():
                course = get_object_or_404(Courses, id=course_id)
                staff = get_object_or_404(CustomUser, id=staff_id)
                subject = Subjects.objects.create(
                    subject_code=subject_code,
                    subject_name=subject_name,
                    course_id=course,
                    staff_id=staff,
                )
                messages.success(request, "ADDED SUBJECT DETAILS!")
                return HttpResponseRedirect("/add_subject")
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD SUBJECT DETAILS - " + str(e))
            return HttpResponseRedirect("/add_subject")
    
    
@api_view(['POST'])
def add_course_form_api(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def edit_admin(request,admin_id):  
    admin = AdminHOD.objects.get(admin=admin_id)
    return render(request,"hod_template/edit_admin_template.html",{"admin":admin})
    
def edit_staff(request,staff_id):  
    staff = Staff.objects.get(admin=staff_id)
    courses = Courses.objects.all()
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff,'courses':courses})

def edit_student(request,student_id):  
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()
    return render(request,"hod_template/edit_student_template.html",{"student":student, "courses":courses})

def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/edit_subject_template.html",{"subject":subject,"staffs":staffs,"courses":courses})

def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course})


def edit_session(request, session_year_id):
    session_year = SessionYearModel.objects.get(id=session_year_id)
    if request.method == 'POST':
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')
        try:
            #updating to new values
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()

            messages.success(request, 'SESSION YEAR UPDATED!')
            return HttpResponseRedirect("/edit_session/"+ str(session_year_id))
        except Exception as e:
            messages.error(request, 'SESSION YEAR UPDATE FAILED - '+ str(e))
    return render(request, 'hod_template/edit_session_template.html', {'session_year': session_year})


@api_view(['PUT', 'POST'])
def update_course(request, course_id):
    try:
        course = Courses.objects.get(id=course_id)
    except Courses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def add_session(request):
    return render(request,"hod_template/add_session_template.html")

def manage_session(request):
    session = SessionYearModel.objects.all()
    return render(request,"hod_template/manage_session_template.html",{"sessionyearmodel":session})

@api_view(['POST'])
def add_session_form_api(request):
    serializer = SessionYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
def edit_admin_form(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        admin_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        address = request.POST.get("address")
        
        try:
            user = CustomUser.objects.get(id=admin_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()
            
            admin_model = AdminHOD.objects.get(admin=admin_id)
            admin_model.address = address
            admin_model.gender = gender
            admin_model.save()
            
            messages.success(request,"SUCCESSFULY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_admin/"+admin_id)
        except Exception as e:
            messages.error(request,"FAILED TO UPDATE THE DETAILS " +str(e))
            return HttpResponseRedirect("/edit_admin/"+admin_id)  

def edit_staff_form(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        department_id = request.POST.get('department_id')
        address = request.POST.get("address")
        
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()
            
            staff_model = Staff.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.gender = gender
            staff_model.department_id = department_id
            staff_model.save()
            
            messages.success(request,"SUCCESSFULY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        except Exception as e:
            messages.error(request,"FAILED TO UPDATE THE DETAILS " +str(e))
            return HttpResponseRedirect("/edit_staff/"+staff_id) 
        

def edit_student_form(request):
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
        
    
def edit_subject_form(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get("subject_name")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")
        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name= subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            subject.save() 
            
            messages.success(request,"SUCCESSFULY UPDATED THE DETAILS")
            return HttpResponseRedirect("/edit_subject/"+subject_id)
        except Exception as e:
            messages.error(request,"FAILED TO UPDATE THE DETAILS "+str(e))
            return HttpResponseRedirect("/edit_subject/"+subject_id) 
        
def replyto_staff_feedback(request):
    staff_feedback = FeedbackStaff.objects.all()
    return render(request,"hod_template/replyto_staff_feedback.html",{"staff_feedback":staff_feedback})  

def replyto_student_feedback(request):
    student_feedback = FeedbackStudent.objects.all()
    return render(request,"hod_template/replyto_student_feedback.html",{"student_feedback":student_feedback})
 
@csrf_exempt
def student_feedback_reply_msg(request):
    feedback_id = request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedbackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    

@csrf_exempt
def staff_feedback_reply_msg(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedbackStaff.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    
    
def student_leave_status(request):
    leaves=StudentLeave.objects.all()
    return render(request,"hod_template/student_leave_status.html",{"leaves":leaves})

def staff_leave_status(request):
    leaves=StaffLeave.objects.all()
    return render(request,"hod_template/staff_leave_status.html",{"leaves":leaves})
    
def approve_student_leave(request,leave_id):
    leave=StudentLeave.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_status"))

def disapprove_student_leave(request,leave_id):
    leave=StudentLeave.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_status"))


def approve_staff_leave(request,leave_id):
    leave=StaffLeave.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_status"))

def disapprove_staff_leave(request,leave_id):
    leave=StaffLeave.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_status"))
    
def hod_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    hod=AdminHOD.objects.get(admin=user)
    return render(request,"hod_template/hod_profile.html",{"user":user,"hod":hod})

def edit_hod_profile_form(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("edit_hod_profile_form"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        
        try:
            user=CustomUser.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            
            user.save()

            messages.success(request, "SUCCESSFULY UPDATED DETAILS!")
            return HttpResponseRedirect(reverse("hod_edit_profile"))
        except Exception as e:
            messages.error(request, "FAILED TO UPDATE DETAILS - " +str(e))
            return HttpResponseRedirect(reverse("hod_edit_profile")) 

def hod_edit_profile(request):
    return render(request,"hod_template/hod_edit_profile.html")  

@csrf_exempt
def delete_course_save(request, course_id):
    try:
        course = Courses.objects.get(id=course_id)
    except Courses.DoesNotExist:
        return JsonResponse({'error': f'Course object with id {course_id} does not exist'}, status=404)
    
    #if request.method == 'DELETE':
    course.delete()
    return JsonResponse({'success': f'Course object with id {course_id} has been deleted'})
    #messages.success(request,"SUCCESSFULY DELETED THE DETAILS")
    #return HttpResponseRedirect("/delete_course/"+course_id)
    #else:
        #return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def delete_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/delete_course_template.html",{"course":course})
    


        
        