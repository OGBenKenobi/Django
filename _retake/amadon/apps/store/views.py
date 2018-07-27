from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.urlresolvers import reverse

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store/index.html', context)

def buy(request):
    if 'quantity' not in request.session:
        request.session['quantity'] = int(request.POST['quantity'])
    else:
        request.session['quantity'] = request.session['quantity'] + int(request.POST['quantity'])
    if 'total'not in request.session:
        request.session['total'] = Product.objects.get(id= request.POST['product_id']).price * float(request.POST['quantity'])
    else:
        request.session['total'] = request.session['total'] + (Product.objects.get(id= request.POST['product_id']).price * float(request.POST['quantity']))
        request.session['charged'] = Product.objects.get(id= request.POST['product_id']).price
    print('I made it through buy-------------------------------------------------------------------')
    return render(request, 'store/checkout.html')

def checkout(request):
    return render(request,'store/checkout.html')
