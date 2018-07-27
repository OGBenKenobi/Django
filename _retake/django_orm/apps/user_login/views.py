from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render('user_login/index.html')