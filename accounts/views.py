from django.contrib import messages
from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['Username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['Firstname']
        lastname=request.POST['Lastname']
        username=request.POST['Username']
        email=request.POST['email']
        password=request.POST['psw']
        password2=request.POST['psw-repeat']
        # myuser=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
        # myuser.save()
        # return redirect('/')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                myuser=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                myuser.save()
                print("user created")
        else:
            print("password not match")
            return redirect('register')
        return redirect('/')

    else:

        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')