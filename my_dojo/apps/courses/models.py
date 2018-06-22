from django.db import models
# Create your models here.
class Course(model.Models):
    name        = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    created_at  = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)