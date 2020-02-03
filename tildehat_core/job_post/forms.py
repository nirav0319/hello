# django

from django import forms
from django.forms import ModelForm

# app
from .models import JobPost


class JobPostForm(forms.ModelForm):

    class Meta:
        model = JobPost
        job_post_fields = [f.name for f in JobPost._meta.get_fields()]
        job_post_fields.remove('date') # date is the post date - added by default
        job_post_fields.remove('user') # the user is the current logged in user - added in views
        fields = tuple(job_post_fields)

