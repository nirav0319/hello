# django
from django.urls import path

# app
from . import views

from django.conf.urls import url


urlpatterns = [
  path('job_post/', views.job_post, name='job_post'),
]