# django
from django.urls import path

# app
from . import views

from django.conf.urls import url


urlpatterns = [
  path('job_search/', views.open_job_search_page, name='job_search'),
  path('job_search/?q=<str:query>', views.open_job_search_page, name='job_search'),
  path('successfull/', views.job_apply, name='applied_successfull'),
]
