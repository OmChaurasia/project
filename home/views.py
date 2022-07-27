import email
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is about page")
def contact(request):
    return HttpResponse("this is contact page")
def handlesignup(request):
    if request.method=="POST":
        signupusertype = request.POST.get('signupusertype')
        signupusername = request.POST.get('signupusername')
        signupuseremail = request.POST.get('signupuseremail')
        signuppwd1 = request.POST.get('signuppwd1')
        signuppwd2 = request.POST.get('signuppwd2')
        print(signuppwd1)
        print(signuppwd2)
        print(signupuseremail)
        print(signupusername)
        print(signupusertype)
        u = User.objects.create_user(username=signupusername, email=signupuseremail, password=signuppwd1)
        u.typeofuser=signupusertype
        u.save()
        return HttpResponse("Account Created")
    else:
        return HttpResponse("Get request is not allowed")