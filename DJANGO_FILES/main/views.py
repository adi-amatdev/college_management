from django.shortcuts import render,HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    return render(request,'main.html')

def dashboard(request):
    return render(request,'dashboard.html')

 
def signup(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        password = request.POST['password']
        confirmpassword =  request.POST['confirmpassword']
        email = request.POST['email']
        
        if(password == confirmpassword):
            if User.objects.filter(username=usn).exists():
                messages.info(request,'USN ALDREDY EXISTS! PLEASE RETRY!')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'USER WITH THIS EMAILID EXISTS!')
                return redirect('/')
            else:
                user = User.objects.create_user(username=usn,password=password,email=email)
                user.save()
                print("User Created")
                return redirect('/')
        else:
            messages.info(request,"PASSWORD NOT MATCHING!")
            return redirect('/')
        
        
    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        password = request.POST['password']
        user = auth.authenticate(username=usn,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('/dashboard/')  
        else:
            messages.info(request,"INVALID CREDENTIALS! PLEASE TRY AGAIN!")
            return redirect('/') 
    
    else:
        return render(request,'home.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/') 

