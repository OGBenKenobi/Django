from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels/$', views.success),
    url(r'^travels/new/$', views.new),
    url(r'^travels/show/(?P<id>\d+)$', views.show),
    url(r'^create$', views.create), 
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    url(r'^logout/$', views.logout),
    url(r'^join/(?P<id>\d+)/$', views.join),
    url(r'^cancel/(?P<id>\d+)/$', views.cancel),
]