from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={

    }

    return render(request, 'home.html', context)

def students(request):
    students = Student.objects.all()
    context={
        'students':students,
    }

    return render(request, 'students.html', context)

def teachers(request):
    teachers = Teacher.objects.all()
    context={
        'teachers':teachers,
    }

    return render(request, 'teachers.html', context)

def studentform(request):
    context = {

    }

    if request.method == "POST": # check for button click
        form = StudentForm(request.POST)
        if form.is_valid():
            context = ""
            for name, value in form.cleaned_data.items():
                print("{}: ({} {}".format\
                    (name, type(value), value))

        requests = form.save(commit=False) # save data locally but not to the database yet

        # save each field to a local variable
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middlename = form.cleaned_data['middlename']
        grade = form.cleaned_data['grade']

        requests.save() # save to the database

        #confirmation message
        messages.success(request, "New student added successfully.")

    else: # show a blank form
        form = StudentForm()
    
    return render(request, 'studentform.html', {"method": request.method, "form": form})

def teacherform(request):
    context = {

    }

    if request.method == "POST": # check for button click
        form = TeacherForm(request.POST)
        if form.is_valid():
            context = ""
            for name, value in form.cleaned_data.items():
                print("{}: ({} {}".format\
                    (name, type(value), value))

        requests = form.save(commit=False) # save data locally but not to the database yet

        # save each field to a local variable
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        subject = form.cleaned_data['subject']
        roomnum = form.cleaned_data['roomnum']

        requests.save() # save to the database
        
        #confirmation message
        messages.success(request, "New teacher added successfully.")

    else: # show a blank form
        form = TeacherForm()
    
    return render(request, 'teacherform.html', {"method": request.method, "form": form})