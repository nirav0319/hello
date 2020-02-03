
from django.conf.urls import url
from . import views



urlpatterns = [
  url(r'^jobcreate/$', views.job_post, name='create_jobs'),
  url(r'^jobupdate/(?P<job_id>\d+)/$', views.job_update, name='update_jobs'),
  url(r'^jobdelete/(?P<job_id>\d+)/$', views.job_delete, name='delete_jobs'),
]
