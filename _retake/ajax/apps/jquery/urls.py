from django.conf.urls import url
from . import views  
         
urlpatterns = [
    url(r'^$', views.jquery_index),
     url(r'^home$', views.jquery_index),
    url(r'^functions$', views.functions_index),      
]