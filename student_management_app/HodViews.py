from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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
from django.shortcuts import render, redirect
from .models import StudentTestScore
import pandas as pd
from django.shortcuts import render
from .models import User
from .models import Subject
from datetime import datetime
from datetime import date






def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")


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

class RetrieveCourseAPIView(RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
    #lookup_field = 'id'


class UpdateCourseAPIView(UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
    
    
class DestroyCourseAPIView(DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
    #lookup_field = 'id'
    
class CourseListView(ListModelMixin, GenericAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class CourseDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def add_student(request):
    courses = Courses.objects.all()
    session_years = SessionYearModel.objects.all()
    return render(request,"hod_template/add_student_template.html",{"courses":courses, "session_years":session_years})

class CreateStudentAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

class RetrieveStudentAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    #lookup_field = 'id'


class UpdateStudentAPIView(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    #lookup_field = 'id'
    
class DestroyStudentAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()
    #lookup_field = 'id'
    
class StudentListView(ListModelMixin, GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class StudentDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def add_subject(request):
    courses = Courses.objects.all()
    #staffs = CustomUser.objects.filter(user_type=2)
    staffs = CustomUser.objects.all()
    return render(request,"hod_template/add_subject_template.html",{"staffs":staffs, "courses":courses})

class CreateSubjectAPIView(CreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subjects.objects.all()

class RetrieveSubjectAPIView(RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subjects.objects.all()
    #lookup_field = 'id'


class UpdateSubjectAPIView(UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subjects.objects.all()
    #lookup_field = 'id'
    
class DestroySubjectAPIView(DestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subjects.objects.all()
    #lookup_field = 'id'
    
class SubjectListView(ListModelMixin, GenericAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class SubjectDetailView(RetrieveModelMixin, GenericAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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


class AddStaffFormAPIView(APIView):
    def post(self, request):
        serializer = AddStaffFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddStudentFormAPIView(APIView):
    def post(self, request):
        serializer = AddStudentFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
    
def edit_staff(request,staff_id):   #need to do it thorugh api
    staff = Staff.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff})

def edit_student(request,student_id):   #need to do it thorugh api
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

def manage_session(request):
    return render(request,"hod_template/manage_session_template.html")

@api_view(['POST'])
def add_session_form_api(request):
    serializer = SessionYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''@api_view(['PUT', 'POST'])
def update_staff(request, staff_id):
    try:
        instance1 = Staff.objects.get(id=staff_id)
        instance2 = CustomUser.objects.get(id=staff_id)
    except (Staff.DoesNotExist, CustomUser.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer1 = StaffSerializer(instance1, data=request.data)
    serializer2 = CustomUserSerializer(instance2, data=request.data)
    serializer1.is_valid()
    serializer2.is_valid()
    if serializer1.is_valid() and serializer2.is_valid():
        serializer1.save()
        serializer2.save()
        return Response(serializer1.data, serializer2.data)
    else:
        errors = {
            "staff_errors": serializer1.errors,
            "customuser_errors": serializer2.errors,
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)'''
        
'''@api_view(['PUT', 'POST'])
def update_staff(request, staff_id):
    try:
        instance1 = Staff.objects.get(id=staff_id)
        instance2 = CustomUser.objects.get(id=staff_id)
    except (Staff.DoesNotExist, CustomUser.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer1 = StaffSerializer(instance1, data=request.data)
    serializer2 = CustomUserSerializer(instance2, data=request.data)
    serializer1.is_valid()
    serializer2.is_valid()
    if serializer1.is_valid() and serializer2.is_valid():
        serializer1.save()
        serializer2.save()
        return Response(serializer1.data, serializer2.data)
    else:
        errors = {
            "staff_errors": serializer1.errors,
            "customuser_errors": serializer2.errors,
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)'''
 
@api_view(['PUT', 'PATCH', 'POST', 'OPTIONS'])
def update_staff(request, staff_id):
    try:
        staff = Staff.objects.get(id=staff_id)
    except Courses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateStaffFormSerializer(staff, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.shortcuts import get_object_or_404

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            subject_code = row['subject_code']
            subject = get_object_or_404(Subject, subject_code=subject_code)
            username = row['usn']
            username = get_object_or_404(User, username=username)

            test_date = row['test_date']
            test_date = date.fromordinal(test_date)
            test_date_str = test_date.strftime('%Y-%m-%d')
            test1 = row['test1']
            test2 = row['test2']
            test3 = row['test3']
            attendance = row['attendance']
            score = StudentTestScore(
                subject_code=subject,
                usn=username,
                test_date=test_date_str,
                test1=test1,
                test2=test2,
                test3=test3,
                attendance=attendance
            )
            score.save()
        return render(request,'success.html')
    return render(request, 'upload.html')

def dump_student_n_staff_info(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        df = pd.read_excel(myfile)
        for index, row in df.iterrows():
            user = User(
                password=row['password'],
                username=row['username'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                user_type=row['user_type'],
            )
            user.save()
        return render(request, 'success.html')
    return render(request, 'dump_student_n_staff_info.html')


def dump_sub(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        df = pd.read_excel(myfile)                      #for specific sheet include : ,sheet_name='Sheet1' in the paranthesis
        for index, row in df.iterrows():
            subject = Subject(
                subject_name=row['subject_name'],
                course_id_id=row['course_id_id'],
                staff_id_id=row['staff_id_id'],
                subject_code=row['subject_code']
            )
            subject.save()
        return render(request, 'success.html')
    return render(request, 'dump_sub.html')









        



