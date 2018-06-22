from django.shortcuts import render, HttpResponse, redirect
from time import time,strftime
import random

def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    elif 'activities' not in req.session:
        req.session['activities'] = []
    
    return render(req,'game/index.html')

def process_gold(req):
    now = strftime('%b %d %Y %H:%M:%S')
    if 'farm' in req.POST:
        rand = random.randrange(10,21)
        req.session['gold'] += rand
        req.session['activities'] = req.session['activities'] + [f'<p class="green">Earned {rand} gold from the Farm! ({now})</p>']
    if 'cave' in req.POST:
        rand = random.randrange(5,11)
        req.session['gold'] += rand
        req.session['activities'] = req.session['activities'] + [(f'<p class="green">Earned {rand} gold from the Cave! ({now})</p>')]
    if 'house' in req.POST:
        rand = random.randrange(2,6)
        req.session['gold'] += rand
        req.session['activities'] = req.session['activities'] + [(f'<p class="green">Earned {rand} gold from the House! ({now})</p>')]
    if 'casino' in req.POST:
        luck = random.randrange(0,3)
        rand = random.randrange(0,51)
        if luck == 0:
            req.session['gold'] += rand
            req.session['activities'] = req.session['activities'] + [(f'<p class="green">Entered Casino and earned {rand} gold! ({now})</p>')]
        else:
            if req.session['gold'] - rand < 0:
                req.session['gold'] = 0
                req.session['activities'] = req.session['activities'] + [(f'<p class="red">Entered Casino and lost all of your gold! ({now})</p>')]
            else: 
                req.session['gold'] -= rand
                req.session['activities'] = req.session['activities'] + [(f'<p class="red">Entered Casino and lost {rand} gold... Ouch.. ({now})</p>')]
    return redirect('/')