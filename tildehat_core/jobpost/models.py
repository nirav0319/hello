from django.db import models
from django.conf import settings
from datetime import datetime


class JobList(models.Model):
    job_id = models.AutoField(primary_key = True)
    user_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.DO_NOTHING,
                            related_name='posted_by'
                            )
    job_description = models.CharField(max_length = 255)
    walk_in = models.BooleanField(default = False)
    offer_to = models.CharField(max_length = 100,blank  = True)
    date = models.DateTimeField(default = datetime.now, editable = True)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.job_description


class AppliedCandiate(models.Model):
    cadidate_id = models.AutoField(primary_key = True)
    job_post_user_info = models.ForeignKey(JobList,
                            on_delete=models.DO_NOTHING,
                            related_name='job_post_user'
                            )
    student_details = models.EmailField()
