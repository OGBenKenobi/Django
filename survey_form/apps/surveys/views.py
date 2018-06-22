from django.shortcuts import render, HttpResponse,redirect

def index(request):
    return render(request,'surveys/index.html')

def submit(request):
    print(request.POST)
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['language']
        request.session['comment'] = request.POST['comments']
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request,'surveys/results.html')