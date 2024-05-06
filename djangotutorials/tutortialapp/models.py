from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    GRADES = (
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    firstname = models.CharField(max_length=200,null=True, verbose_name="First Name")
    lastname = models.CharField(max_length=200,null=True, verbose_name="Last Name")
    middlename = models.CharField(max_length=200,null=True, verbose_name="Middle Name(s)")
    grade = models.CharField(max_length=200,null=True, choices=GRADES, verbose_name="Grade")

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"

class Teacher(models.Model):

    SUBJECTS = (
        ('ELA', 'ELA'),
        ('Social Studies', 'Social Studies'),
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('Foreign Language', 'Foreign Language'),
        ('Business', 'Business'),
        ('PE', 'PE'),
    )

    firstname = models.CharField(max_length=200,null=True, verbose_name="First Name")
    lastname = models.CharField(max_length=200,null=True, verbose_name="Last Name")
    subject = models.CharField(max_length=200,null=True, choices=SUBJECTS, verbose_name="Subject")
    roomnum = models.IntegerField(verbose_name="Room Number")

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200,null=True, verbose_name="First Name")
    lastname = models.CharField(max_length=200,null=True, verbose_name="Last Name")

    def __str__(self) -> str:
        return f"{self.lastname}, {self.firstname}"