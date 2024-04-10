# django_project

## Step 1: Create a Project

- `django-admin startporject [project name here]`
- Python 3.9 -> `python -m django startproject [project name here]`

## Step 2: Create an App

- `djang-admin startapp [app name here]`
- Python 3.9 -> `python manage.py startapp [app name here]`

## Step 3: Run the Web Server

- cd into the project folder that contains manage.py
- run `python manage.py runserver`

## Step 4: Build the Database

- cd into the project folder that contains manage.py
- run `python manage.py migrate`

## Step 5: Create Super User

- cd into the project folder that contains manage.py
- run `python manage.py createsuperuser`

## Step 6: Add App to settings.py Install App Dictionary

```python
INSTALLED_APPS = [

...

    'app_name',

]
```

## Step 7: Add template folder to settings.py Templates

```python
'DIRS': [BASE_DIR / 'templates'],
```

## View Function
```python
def base(request):

   context={

    }

    return render(request, 'base.html', context)
```

## Step 8: Add app url.py to project url.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutortialapp.urls'))
]
```

## Step 9: Add app urls.py to app folder

```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
]
```

## Inheriting Code from a Template:

### In base.html
```python
{% block content %}

{% endblock %}
```

### In template
```python
{% extends 'base.html'%}
```
## Making Changes to the Database

### 1: Saving Changes
`python manage.py makemigrations`

### 2: Build Changes into Database
`python manage.py migrate`

