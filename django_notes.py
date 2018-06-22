# Create virtual environment with Django in terminal
> virtualenv -p python3 djangoPy3Env
> source djangoPy3Env/bin/activate
(djangoPy3Env)> pip install Django==1.10

# Create a new project
# Navigate to a location where you want to create your project
> django-admin startproject project_name

# Navigate into the main directory that you just created
> cd project_name
# Make a new apps directory
> mkdir apps
# Navigate into apps
> cd apps

# Next you'll create an __init__.py file
> touch __init__.py

# Create new app
> python ../manage.py startapp new_app

# In settings.py (this file lives inside the main directory. The main directory is alongside apps and manage.py) we are going to have to add our application to the project. That means adding apps.new_app to our INSTALLED_APPS list:
# Inside main/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# BECOMES:
INSTALLED_APPS = [
    'apps.new_app', ### added this line!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Go to your main folder and run python manage.py runserver from the terminal. Then proceed to localhost:8000
# Navigate to urls.py within project_name folder to allow urls.py within apps/new_app to be accessed

from django.conf.urls import url, include  # Notice we added include  
# comment out or delete the line below, we will not be using the admin module
# from django.contrib import admin
# Why won't we use the admin module? Because we're focusing on how to code, 
# not on how to help people who do not know how to code how to manage the app.
urlpatterns = [
    url(r'^', include('apps.new_app.urls')) # And now we use the include function to pull in our new_app.urls...
]

# Our app's urls file doesn't exist yet. Let's make it. From the command line:

> cd apps/new_app
> touch urls.py

# Open urls.py in your text editor. Add the code below:

# apps/first_app/urls.py

from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index)   # This line has changed! Notice that urlpatterns is a list, the comma is in
]                            # anticipation of all the routes that will be coming soon

#apps/first_app/views.py

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
response = "Hello, I am your first request!"
return HttpResponse(response)

#Template Rendering
#In our views file, Django knows to look in the templates folder first for whatever path we pass to our render method.

# views.py
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "ourApp/index.html", context)

#html
<!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>Index</title>
      {% load static %}
      <!-- The line above tells Django to be ready to listen for static files -->
      <link rel="stylesheet" href="{% static 'ourApp/css/main.css' %}">
      <!-- Put the static files in the static folder inside your app.  
           Django collects files within all static folders and puts them within a single folder -->    
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>{{email}} and {{name}}</p>
    </body>
  </html>


#Session
#To set up session in our terminal, head to the directory where manage.py resides and run the following commands:
  # Need to be in same directory as manage.py file
  > python manage.py makemigrations
  > python manage.py migrate

#now we can restart our server and uses session (request.session)
# As request.session is just a dictionary, you can attach any key/value pairs.  For example, in the views.py file, you could do:

request.session['name'] = request.POST['name']
request.session['counter'] = 100

# In the html file, Django lets you directly access request.session.  For example to access request.session['name'], simply do

{{request.session.name}}

# Useful session methods:
    request.session['key']
        This will retrieve (get) the value stored in key
    request.session['key'] = 'value'
        Set the value that will be stored by key
    del request.session['key']
        Deletes a session key if it exists, throws a keyError if it doesn’t. Use along with try and except since it’s better to ask for forgiveness than permission
    'key' in request.session
        Returns a boolean of whether a key is in session or not
    {{ request.session.name }}
        Use dot notation (.) to access request.session keys from templates since square brackets ([]) aren’t allowed there

#Models

#To implement models, implement code similar to the following in the apps models.py
# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
      name = models.CharField(max_length=255)
      desc = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
  class Comment(models.Model):
      comment = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # Notice the association made with ForeignKey for a one-to-many relationship
      # There can be many comments to one blog
      blog = models.ForeignKey(Blog, related_name = "comments")
  class Admin(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      blogs = models.ManyToManyField(Blog, related_name = "admins")
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

#Column Types
CharField
    # Any text that a user may enter. This has one additional required parameter, max_length, that (unsurprisingly) is the maximum length of text that can be saved.
TextField
    # Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter series into the field, and it would save in the database correctly.
IntegerField, BooleanField
    # Holds integers or booleans, respectively
DateTimeField
    # Used for date and times, such as timestamps or when a flight is scheduled to depart. This field can take two very useful optional parameters, auto_now_add=True, which adds the current date/time when object is created, and auto_now=True, which automatically updates any time the object is modified.
ForeignKey, ManyToManyField, OneToOneField
    # Used to indicate a relationship between models (anything that would require a JOIN statement in SQL). ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just as the foreign key column goes in the SQL table on the "many" side.

#ManyToManyField

class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

#It doesnt matter which model has the ManyToManyField. The model would still work if the Book model has a field named publishers instead.

#Add a relationship in shell:
this_book = Book.objects.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)


#Forward the addition, deletion or edit of the models, use migrate function in terminal
  > python manage.py makemigrations
  > python manage.py migrate

#to import app data to shell run the following:
>>> from apps.{{app_name}}.models import * #*imports all. can specify model

# Creating a new record
   Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
        Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
        Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field
    Alternative way of creating a record
        b = Blog(name="Disney Blog", desc="Disney stuff")
        b.name = "Disney Blog!"
        b.desc = "Disney stuff!!!"
        b.save()
# Basic Retrieval
    Blog.objects.first() - retrieves the first record in the Blog table
    Blog.objects.last() - retrieves the last record in the Blog table
    Blog.objects.all() - retrieves all records in the Blog table
    Blog.objects.count() - shows how many records are in the Blog table
# Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
    b = Blog.objects.first() # gets the first record in the blogs table
    b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
    b.save() # updates the blog record
# Deleting the record - use delete().  For example
    b = Blog.objects.get(id=1)
    b.delete() # deletes that particular record
# Other methods to retrieve records
    Blog.objects.get(id=1) - retrieves where id is 1; get() retrieves one and only one record. It will return an error if it finds fewer than or more than one match.
    Blog.objects.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
    Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
    Blog.objects.order_by("created_at") - orders by created_date field
    Blog.objects.order_by("-created_at") - reverses the order
    Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
    Blog.objects.first().comments.all() - grabs all comments from the first Blog
    Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
    Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to
# Setting Relationship
    Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).

1. Create project and app
2. Install app (settings.py)
3. Models
4. urls
    #index.html
    Register
        Post/redirect
        Get/redirect
    Login
        Post/redirect
5. Templates

#ex
def index(request):
    render(request,'index.html')
def register(request):
    redirect('/')

#corresponding urls
url(r'^$', views.index)
url(r'^register/$', views.register)

#Validations

# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = BlogManager()
    # *************************

# Now in our views.py file, we can use Blog.objects.basic_validator(postData):

# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
def update(request, id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Blog.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/blog/edit/'+id)
        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            messages.success(request, "Blog successfully updated)
            # redirect to a success route
            return redirect('/blogs')

#bcrypt

# Review Bcrypt
# In an extremely simplified sense, Bcrypt implements an algorithm that takes longer to generate a hashed string, in addition to generating a random, unique salt per password. Why is this better? Any malicious user who wants to generate every possible hashed output would be stuck trying to create a rainbow table for years instead of days. Bcrypt also has the ability to scale the time it takes to hash a string, meaning as computers get faster, Bcrypt can become more complex and time-consuming in return.

# Installation (from within virtualenv)
(djangoPy3Env) pip install bcrypt

#Usage
#1 The passwords must be hashed with salt before being inserted into the database.
#2. To compare passswords to verify a user, the user input must be hashed with the same salt and comared. If the hashed passwords match, then the user is logged in.

#Ex. In shell
>>> import bcrypt
>>> hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
>>> print(hash1)
$2b$12$Wdc2qwiP6u0WdQdKwmer7.DMIcY6q76GxvrJgaodnpRDmpP8mwkDa

# To check if a password encrypted in bcrypt matches another, we can use the `bcrypt.checkpw` method
>>> bcrypt.checkpw('test'.encode(), hash1)
True

# In an application, however, hash1 would be fetched from the database and would need to be encoded again, such as in the following snippet:
def validate_login(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
        print("password match")
    else:
        print("failed password")                    