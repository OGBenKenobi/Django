from django.shortcuts import render, HttpResponse,redirect
from .models import Product

def index(request):
    return render(request,'store/index.html',{ 'products': Product.objects.all()})

def buy(request):
    if 'count' not in request.session:
        request.session['count'] = int(request.POST['quantity'])
    else:
        request.session['count'] = request.session['count'] + int(request.POST['quantity'])
    if 'total'not in request.session:
        request.session['total'] = Product.objects.get(id= request.POST['prod']).price * float(request.POST['quantity'])
    else:
        request.session['total'] = request.session['total'] + (Product.objects.get(id= request.POST['prod']).price * float(request.POST['quantity']))
    request.session['charged'] = Product.objects.get(id= request.POST['prod']).price
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'store/checkout.html')
