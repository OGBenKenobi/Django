from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^books/$', views.books),
    url(r'^logout/$', views.logout),
    url(r'^books/add/$', views.booksAdd),
    url(r'^books/add/addbooks/$', views.addBooks),
    url(r'^book/(?P<id>\d+)/$', views.book),
    url(r'^book/(?P<id>\d+)/addreview/$', views.addReview),
    url(r'^users/(?P<id>\d+)/$', views.users),
]