from django.db import models
from ..login_register.models import User

class Schedule(models.Model):
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    date_start  = models.DateTimeField()
    date_end    = models.DateTimeField()
    plan        = models.CharField(max_length=255)
    creator     = models.ForeignKey(User, related_name="created_trips") 
    trip_members= models.ManyToManyField(User, related_name="joined_trips")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    