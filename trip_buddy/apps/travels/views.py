from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError ##Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
import bcrypt

def success(request):
    return render(request,'travels/index.html')

