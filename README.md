# django_project

## Step 1: Create a Project

- django-admin startporject [project name here]
- Python 3.9 -> python -m django startproject [project name here]

## Step 2: Create an App

- djang-admin startapp [app name here]
- Python 3.9 -> python manage.py startapp [app name here]

## Step 3: Run the Web Server

- cd into the project folder that contains manage.py
- run `python manage.py runserver`

## Step 4: Build the Database

- cd into the project folder that contains manage.py
- run `python manage.py migrate`

## Step 5: Create Super User

- cd into the project folder that contains manage.py
- run `python manage.py createsuperuser`