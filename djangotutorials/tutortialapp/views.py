from django.shortcuts import render
from .models import Student

# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={
        'students':Student.objects.all()
    }

    return render(request, 'home.html', context)