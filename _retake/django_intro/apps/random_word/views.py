from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    context = {
        "rando": get_random_string(length=14),
    }
    return render(request, 'random_word/index.html', context)

def reset(request):
    if 'count' in request.session:
        request.session.pop('count')
    return redirect('/random_word')