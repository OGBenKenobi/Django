from django.shortcuts import render,redirect
from time import time, strftime

def index(request):
    return render(request,'session_words/index.html')

def add(request):
    now = strftime('%b %d %Y %H:%M:%S')
    print(now)
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'big' in request.POST:
        request.session['activity'] = request.session['activity'] + [f'<p class="{request.POST["color"]} {request.POST["big"]}">{request.POST["word"]}<span> -- {now}</span></p>']
    else:
        request.session['activity'] = request.session['activity'] + [f'<p class="{request.POST["color"]}">{request.POST["word"]}<span>-- {now}</span></p>']
    
    print(request.session['activity'])
    return redirect('/words')

def clear(request):
    request.session.flush()
    return redirect('/words')
