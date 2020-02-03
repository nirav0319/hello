from django import forms
from .models import JobList


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ('job_description','walk_in')
