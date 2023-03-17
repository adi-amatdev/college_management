from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from student_management_app.EmailBackEnd import EmailBackEnd

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
            return HttpResponse("Email : "+request.POST.get("email")+ " Password : " + request.POST.get("password") )
        else:
            return HttpResponse("Invalid login")
        
def getuserdetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

    