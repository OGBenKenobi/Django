from django.shortcuts import render, HttpResponse, redirect

def jquery_index(request):
    return render(request, "jquery/jquery_index.html")

def functions_index(request):
    return render(request, "jquery/jquery_functions.html")
