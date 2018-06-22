from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    content = {
        'rando': get_random_string(length=14),
        }
    return render(request, 'word_app/index.html', content)

def reset(request):
    if 'count' in request.session:
        request.session.pop('count')
    return redirect('/random_word')

