from django.conf.urls import url
from . import views        
   
urlpatterns = [
    url(r'^/survey$', views.index),
    url(r'^/survey_submit$', views.survey_submit),
    url(r'^/survey_result$', views.survey_result)  
]  