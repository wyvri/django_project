from socket import fromshare
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'middlename', 'grade']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'subject', 'roomnum']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']