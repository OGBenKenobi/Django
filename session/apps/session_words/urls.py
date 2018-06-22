from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^words/$', views.index),
    url(r'^add/$', views.add),
    url(r'^words/clear/$', views.clear),
]