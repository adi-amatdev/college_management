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
    #lookup_field = 'id'
    
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
    return render(request,"hod_template/add_student_template.html",{"courses":courses})

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
    staffs = CustomUser.objects.filter(user_type=2)
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
def courses_form_submission(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyFormAPIView(APIView):
    def post(self, request):
        serializer = AddStaffFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


        



