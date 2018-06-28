from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError
import bcrypt
from .models import *

def index(request):
    return render(request,'login_registration/index.html')

def books(request):
    content = {
        'reviews': Reviews.objects.all().order_by('-created_at')[:3],
        'reviewed_books' : Book.objects.all()
    }
    x='1'
    for i in range(3):
        for y in range(content['reviews'][i].rating):
            x = x + '1'
        print(x)
    content['rating'] = x

    return render(request,'login_registration/books.html',content)

def login(request):
    try:
        user = User.objects.get(email=request.POST['login_email'])
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id
            return redirect('/books')
    except User.DoesNotExist:
        pass
    messages.error(request, 'Login unsuccessful. Plase check email and passowrd, and try again.', extra_tags='login')
    return redirect('/')

def register(request):
    errors = User.objects.validator(request.POST)
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        try:
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = pwHash)
        except IntegrityError:
            messages.error(request, 'this email already exists', extra_tags='email')
            return redirect('/')
    request.session['first_name'] = request.POST['first_name']
    request.session['id'] = user.id
    return redirect('/books')

def logout(request)    :
    request.session.flush()
    return redirect('/')

def booksAdd(request):
    content = {
        'books': Book.objects.all()
    }
    return render(request,'login_registration/bookAdd.html', content)

def addBooks(request):
    if len(request.POST['newauthor']) > 1:
        book = Book.objects.create(name=request.POST['title'],author=request.POST['newauthor'])
        user = User.objects.get(id = request.session['id'])
        Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
        book.save()
    else:
        book = Book.objects.create(name=request.POST['title'],author=request.POST['author'])
        user = User.objects.get(id = request.session['id'])
        Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
        book.save()
    return redirect(f'/book/{book.id}/')

def addReview(request,id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id = request.session['id'])
    Reviews.objects.create(user=user,book = book,review = request.POST['review'],rating = request.POST['rating'])
    return redirect(f'/book/{book.id}/')

def book(request,id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        messages.error(request,'Book does not exists')
    content = {
        'reviews': book.books_reviewed.all(),
        'book': book
    }
    return render(request,'login_registration/book.html',content)   

def users(request,id):
    user = User.objects.get(id=id)
    content = {
        'user': user,
        'books': User.objects.raw(f'select distinct login_registration_book.id,book_id,name from login_registration_reviews join login_registration_book on login_registration_reviews.book_id = login_registration_book.id  where user_id = {id}'),
        'cnt' : user.reviewed_books.count()
    }
    return render(request,'login_registration/users.html',content)