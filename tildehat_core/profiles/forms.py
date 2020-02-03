# django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm

# app
from .models import TildehatUser


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = TildehatUser
        fields = ('phone_number',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = TildehatUser
        fields = ('phone_number',)


class SignUpForm(UserCreationForm):

    phone_number = forms.CharField(max_length=254, help_text='Required. Enter a valid phone_number')

    class Meta:
        model = TildehatUser
        fields = ('phone_number','first_name','last_name','password1', 'password2','about_me','profile_pic','upload_resume')


class UserUpdateForm(forms.ModelForm):

    phone_number = forms.CharField(max_length=254, help_text='Required. Enter a valid phone_number address.')

    class Meta:
        model = TildehatUser
        fields = ('phone_number', 'ctc')

class RecruiterProfileForm(forms.ModelForm):

    class Meta:
        model = TildehatUser
        fields = ('company', 'designation') # Can do [f.name for f in tildehat_profile._meta.get_fields()] for more automation


class JobPostForm(forms.ModelForm):

    class Meta:
        model = TildehatUser
        fields = ('company', 'designation') # Can do [f.name for f in tildehat_profile._meta.get_fields()] for more automation
