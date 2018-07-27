from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/show$', views.show),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)/delete$', views.destroy),
    url(r'^users/(?P<id>\d+)/update$', views.update),
]