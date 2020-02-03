from django.db import models

# Create your models here.

class JobPost(models.Model):
    """
    Enabling a job post by a user account
    """
    user = models.ForeignKey(
        'profiles.TildehatUser',
        on_delete=models.SET('unlinked'), # Incase the user the deleted, the post is not linked to any account
    )
    jd = models.CharField(max_length=1000, null=True)
    date =  models.DateField(auto_now_add=True)
    role = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    ctc = models.CharField(max_length=100, null=True)
    education = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    openings = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=1000, null=True)
    contact = models.CharField(max_length=100, null=True)