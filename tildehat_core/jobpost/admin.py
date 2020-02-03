from django.contrib import admin
from .models import JobList,AppliedCandiate
# Register your models here.

class JobListAdmin(admin.ModelAdmin):
    list_display = ['user_by','job_description','offer_to','walk_in','date','created_at','updated_at']


class AppliedCandiateAdmin(admin.ModelAdmin):
    list_display = ['job_post_user_info','student_details']




admin.site.register(JobList,JobListAdmin)
admin.site.register(AppliedCandiate,AppliedCandiateAdmin)
