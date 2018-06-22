from django.shortcuts import render
from time import gmtime, strftime

def index(response):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(response,'time_app/index.html', context)
