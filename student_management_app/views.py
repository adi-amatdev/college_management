from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from student_management_app.EmailBackEnd import EmailBackEnd
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response
import requests

from .serializers import *
from .models import *
from django.http import JsonResponse

def showdemopage(request):
    return render(request,"demo.html")

def showloginpage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password = request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request,"Invalid Login Credentials")
            return HttpResponseRedirect("/")
        
def getuserdetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")



            
    
    