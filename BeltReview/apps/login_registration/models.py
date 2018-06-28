from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2 or not  str.isalpha(postData['first_name']):
            errors['first_name'] = 'first name must be at least 2 charachters long and contain no numbers'
        if len(postData['last_name']) < 2 or not str.isalpha(postData['last_name']):
            errors['last_name'] = 'last name must be at least 2 charachters long and contain no numbers'
        if len(postData['email']) < 1 or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'must enter a vlaid email address'
        if len(postData['password']) < 5:
            errors['password'] = 'pasword must be at least 5 charachters'
        if postData['confirm_pw'] != postData['password'] :
            errors['confirm_pw'] = 'your passwords do not match'
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255,unique=True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    
class Book(models.Model):
    name =  models.CharField(max_length = 255)
    author =  models.CharField(max_length = 255)
    book_reviews = models.ManyToManyField(User, through='Reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    user = models.ForeignKey(User,related_name='reviewed_books')
    book = models.ForeignKey(Book, related_name='books_reviewed')
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)