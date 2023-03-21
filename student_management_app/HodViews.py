from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from student_management_app.models import CustomUser, Staff
import requests


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
    


