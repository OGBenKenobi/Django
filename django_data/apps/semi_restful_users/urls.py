from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/(?P<id>\d+)/update$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    url(r'^create$', views.create),
]