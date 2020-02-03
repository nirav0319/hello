# django
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings

# app
from .managers import TildehatUserManager

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.profile_id, filename)

class TildehatUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where email is the unique identifier
    for authentication instead of usernames. This will later
    be linked to a Profile.
    """
    profile_id = models.CharField(max_length = 12,default=uuid.uuid4().hex, editable=False, unique=True)
    phone_number = models.CharField( default="",max_length = 10,unique=True)
    first_name = models.CharField(max_length = 25,default = "")
    last_name = models.CharField(max_length = 25,default = "")
    is_staff = models.BooleanField(default = False)
    is_recruiter = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default = timezone.now)
    profile_pic = models.ImageField(default = 'default.jpg',upload_to = 'user_directory_path/profile_pics')
    about_me = models.TextField(default = " Hi, myself  Name Title working as a software developer in cisco.I have 5 years work experience. I did my btech from IISC Bangalore. I am good at devops, git, jenkins and software development.")
    upload_resume = models.FileField(upload_to = 'user_directory_path/documents',blank = True)



    company = models.CharField(max_length = 30, null = True) # Null ensures that user can add this info any time
    designation = models.CharField(max_length = 30, null = True)
    ctc = models.CharField(max_length = 30, null = True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = TildehatUserManager()

    def __str__(self):
        return self.first_name
