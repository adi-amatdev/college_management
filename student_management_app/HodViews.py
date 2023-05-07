from django.contrib import messages
from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from student_management_app.models import CustomUser, Staff
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction


@login_required
def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")



def add_staff_form_save(request):
    if request.method != "POST":
        return HttpResponse("METHOD NOT ALLOWED")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        admin_id = request.POST.get("admin_id")
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
                staff = Staff.objects.create(admin=user, address=address, admin_id=admin_id)
                messages.success(request, "ADDED STAFF DETAILS!")
                return HttpResponseRedirect("/add_staff")
        except Exception as e:
            with transaction.atomic():
                transaction.set_rollback(True)
                messages.error(request, "FAILED TO ADD STAFF DETAILS - " + str(e))
            return HttpResponseRedirect("/add_staff")


class CreateStaffAPIView(CreateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

class RetrieveStaffAPIView(RetrieveAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    #lookup_field = 'id'


class UpdateStaffAPIView(UpdateAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    #lookup_field = 'id'
    
class DestroyStaffAPIView(DestroyAPIView):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    #lookup_field = 'id'
    
class StaffListView(ListModelMixin, GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class StaffDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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
    admin_id = request.POST.get('admin_id')
    # Create a new user
    try:
        user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username,user_type=3)
        user.save()
    except Exception as e:
        messages.error(request, "FAILED TO ADD STUDENT - " + str(e))
        return redirect('/add_student')
    # Create a new student
    try:
        student = Students.objects.create(admin=user, gender=gender, section=section, address=address, course_id_id=course_id, session_year_id_id=session_year_id_id)
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
    
class AddSubjectFormAPIView(APIView):
    def post(self, request):
        serializer = AddSubjectFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
def edit_staff(request,staff_id):  
    staff = Staff.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff})

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

def edit_session(request,session_year_id):
    session = SessionYearModel.objects.get(id=session_year_id)
    return render(request,"hod_template/edit_session_template.html",{"sessionyearmodel":session})


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
    

def edit_staff_form(request):
    if request.method != 'POST':
        return HttpResponse("<h2>METHOD NOT PERMITTED</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
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
        
def edit_session_form(request):
    pass 
        
        
        