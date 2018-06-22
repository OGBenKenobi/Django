from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Dojo(models.Model):
    name        = models.CharField(max_length=255)
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=2)
    desc        = models.CharField(max_length=255, default="None")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
class Ninja(models.Model):
    dojo_id     = models.IntegerField()
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    ninja_dojo  = models.ForeignKey(Dojo, related_name="ninjas")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)