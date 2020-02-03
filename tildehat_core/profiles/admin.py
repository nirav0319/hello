from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# app
from .forms import UserCreationForm, UserChangeForm
from .models import TildehatUser


class TildeHatUserAdmin(UserAdmin):
    """
    Custom admin that allows us to control all fields of a user
    and his profile
    """
    add_form = UserCreationForm
    form = UserChangeForm
    model = TildehatUser
    list_display = ('phone_number', 'first_name','last_name','is_staff', 'is_active','is_recruiter','ctc')
    list_filter = ('phone_number', 'is_staff', 'is_active','ctc')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password','ctc')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active', 'ctc')}
        ),
    )
    search_fields = ('phone_number','ctc')
    ordering = ('phone_number', 'ctc')


admin.site.unregister(Group) # We are not using groups ... for now
admin.site.register(TildehatUser, TildeHatUserAdmin)
