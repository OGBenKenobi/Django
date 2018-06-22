from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogs_app/index.html", context)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test" 
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    response = "placeholder to display ", number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog ", number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')
