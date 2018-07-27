from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'courses': Course.objects.all() 
    }
    return render(request, 'courses/index.html', context)

def add(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/')

def delete(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, id):
    c = Course.objects.get(id=id)
    c.delete()
    return redirect('/')