from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'surveys/index.html')

def survey_submit(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        print("******I made it through the if******")
        return redirect('/surveys/survey_result')
    else:
        return redirect('/surveys/survey')

def survey_result(request):
    return render(request,'surveys/survey_result.html')


