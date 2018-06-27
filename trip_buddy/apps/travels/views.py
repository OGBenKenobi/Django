from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError ##Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
import bcrypt
from .models import *

def success(request):
    context = {
        'schedules': Schedule.objects.all()
    }
    return render(request,'travels/index.html', context)

def new(request):
    return render(request, 'travels/new.html')

def create(request):
    user = User.objects.get(id=request.session['id'])
    Schedule.objects.create(city = request.POST['new_city'], state = request.POST['new_state'], date_start = request.POST['new_date_start'], date_end = request.POST['new_date_end'], plan = request.POST['description'], creator = user)
    return redirect('/travels')

def destroy(request,id):
    Schedule.objects.get(id=id).delete()
    return redirect('/travels')

def show(request, id):
    context = { 
        'schedule': Schedule.objects.get(id=id)
    }
    return render(request,'travels/show.html', context)
