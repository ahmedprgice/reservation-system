from django.shortcuts import render, redirect
from .forms import StudentForm, StaffForm, LoginAuthForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Student, Staff
# Create your views here.

def register(response):
    return render(response, "register/register.html",{})

def register_student(response):
    if response.method == "POST":
        form = StudentForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            messages.success(response, 'Student registered successfully!')
            return redirect("/home")
        else:
            # Add debug print statements
            print("Form errors: ", form.errors)
            messages.error(response, 'Error registering student: {}'.format(form.errors))
    else:
        form = StudentForm()
    return render(response, "register/register_student.html", {"form": form})

def register_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff registered successfully.')
            return redirect("/home")
        else:
            # Add debug print statements
            print("Form errors: ", form.errors)
            messages.error(request, 'Error in staff registration.')
    else:
        form = StaffForm()
    return render(request, "register/register_staff.html", {"form": form})


def user_login(response):
    if response.method == "POST":
        form = LoginAuthForm(response, data=response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                messages.success(response, 'You are now logged in')
                return redirect("/home")
            else:
                messages.error(response, 'Invalid username or password')
    else:
        form = LoginAuthForm()
    return render(response, "register/login.html", {"form":form})
    


