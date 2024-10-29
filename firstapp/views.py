from django.http import JsonResponse
from django.shortcuts import render,redirect
from firstapp.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
import json


def home(request):
    return render(request,"ekart/index.html")

def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

def login(request): 
    if request.user.is_authenticated:       
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                auth_login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"ekart/login.html")
 
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now..!")
            return redirect('/login')
    return render(request,"ekart/register.html",{'form':form})

