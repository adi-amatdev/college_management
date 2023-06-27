from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from student_management_app.EmailBackEnd import EmailBackEnd
from rest_framework.decorators import api_view
from rest_framework import status 
from .models import *




def showloginpage(request):
    return render(request,"main_login.html")


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get("email"),password = request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect('staff_home')
            else:
                return HttpResponseRedirect('student_home')
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




            
    
    