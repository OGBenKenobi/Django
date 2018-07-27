from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'semi_restful_users/index.html', context)

def new(request):
    return render(request, 'semi_restful_users/new.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_restful_users/edit.html', context)

def show(request, id):
    context ={
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_restful_users/show.html', context)

def create(request):
    User.objects.create(first_name =request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/users')

def destroy(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect('/users')

def update(request, id):
    u = User.objects.get(id=id)
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.save()
    return redirect('/users/'+str(u.id)+'/show' )