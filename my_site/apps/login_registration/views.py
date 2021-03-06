from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError ##Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
import bcrypt
from .models import User

def index(request):
    return render(request,'login_registration/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        try:
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = pwHash)
        except IntegrityError: #Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
            messages.error(request, 'this email already exists', extra_tags='email')
            return redirect('/')
    request.session['first_name'] = request.POST['first_name']
    return redirect('/success')   

def login(request):
    try:
        user = User.objects.get(email=request.POST['login_email'])
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            return redirect('/success')
    except User.DoesNotExist: #https://stackoverflow.com/questions/14255125/catching-doesnotexist-exception-in-a-custom-manager-in-django 
        pass
    messages.error(request, 'Login unsuccessful. Plase check email and passowrd, and try again.', extra_tags='login')
    return redirect('/')

def success(request):
    return render(request,'login_registration/success.html')

