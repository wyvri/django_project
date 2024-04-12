from django.shortcuts import render
from .models import *

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