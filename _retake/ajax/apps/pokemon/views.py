from django.shortcuts import render, HttpResponse, redirect

def index(request):
    num_list = []
    for i in range(1,151):
        num_list.append(i)
    context = {
        "num_list":num_list,
    }
    return render(request, 'pokemon/index.html', context)