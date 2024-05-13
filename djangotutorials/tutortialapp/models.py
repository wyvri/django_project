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

    first_name = models.CharField(max_length=200,null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=200,null=True, verbose_name="Last Name")
    middle_name = models.CharField(max_length=200,null=True, verbose_name="Middle Name(s)")
    grade = models.CharField(max_length=200,null=True, choices=GRADES, verbose_name="Grade")

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"

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

    first_name = models.CharField(max_length=200,null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=200,null=True, verbose_name="Last Name")
    subject = models.CharField(max_length=200,null=True, choices=SUBJECTS, verbose_name="Subject")
    roomnum = models.IntegerField(verbose_name="Room Number")

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="cat.png", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"