from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#app
from .forms import JobPostForm

# Create your views here.



@login_required(login_url='login')
def job_post(request):
    """
    Allows the recruiter to post a job
    """
    if request.user.is_authenticated:
        is_recruiter = request.user.is_recruiter
        company = request.user.TildehatProfile.company
        designation = request.user.TildehatProfile.designation

    if (company is None) or (designation is None):
        return redirect('recruiter_profile')
        
    context = {}
    if request.method == 'POST':    
        form = job_post_form(request.POST)
        # form.fields["user_id"].initial = "abc"
        form.instance.user = request.user

        if form.is_valid():
            # TODO built in form validation
            # TODO add form .user here
            form.save()
            return redirect('recruiter_home')



    j_p_form = job_post_form

    return render(request, 'job_post.html', context = {'j_p_form': j_p_form})