from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import JobList
from .forms import JobListingForm



@login_required(login_url='login')
def job_post(request):
    form = JobListingForm
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            entity = form.save(commit = False)
            entity.user_by = request.user
            entity.save()
            return redirect('recruiter_home')
    return render(request,'jobscreate.html',{'form':form})

@login_required(login_url='login')
def job_update(request,job_id):
    job_data = JobList.objects.get(job_id = job_id)
    form = JobListingForm
    if request.method == 'POST':
        form = JobListingForm(request.POST,instance = job_data)
        if form.is_valid():
            print("form data:",form.cleaned_data['walk_in'])
            form.save()
            return redirect('recruiter_home')
    return render(request,'jobsupdate.html',{'job_data':job_data,'form':form})

@login_required(login_url='login')
def job_delete(request,job_id):
    job_data = JobList.objects.get(job_id = job_id)
    job_data.delete()
    return redirect('recruiter_home')
