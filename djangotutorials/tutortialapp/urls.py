from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('studentform/', views.studentform, name='studentform'),
    path('teacherform/', views.teacherform, name='teacherform'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/login/', views.login, name='login'),
    path("accounts/signup/", views.signup, name="signup"),
]