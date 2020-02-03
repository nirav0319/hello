# django
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tildehat_core.jobpost.models import JobList,AppliedCandiate
from .models import TildehatUser
from django.contrib import messages
#app
from .forms import SignUpForm, UserUpdateForm, RecruiterProfileForm

def signup(request):
    """
    Render a signup form for the user, save the details
    into the database if entered correctly, then login
    and redirect to the job_search page. Has built in
    form validation checks.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # phone_number = form.cleaned_data.get('phone_number')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(phone_number = phone_number, password=raw_password)
            # login(request, user)
            # return redirect('job_search')
    else:
        messages.info(request,"please provide correct information")
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    """
    Render a profile update form for the user, with prefilled
    details. If updated correctly, save and redirect to job_search.
    Has built in form validation checks.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)


        if u_form.is_valid():
            u_form.save()

            return redirect('job_search')

    else:
        u_form = UserUpdateForm(instance=request.user)



    context = {'u_form': u_form}

    return render(request, 'profile.html', context)


@login_required(login_url='login')
def recruiter_profile(request):
    """
    Recruiter profile completion and request for access
    """

    if request.user.is_authenticated:
        is_recruiter = request.user.is_recruiter
        company = request.user.company
        designation = request.user.designation


    if (company is not None) and (designation is not None):
        return redirect('recruiter_home')


    if request.method == 'POST':
        r_p_form = RecruiterProfileForm(request.POST, instance=request.user)

        if r_p_form.is_valid():
            r_p_form.save()
            return redirect('job_search')

    else:
        r_p_form = RecruiterProfileForm(instance=request.user)


    context = {'r_p_form': r_p_form}

    return render(request, 'recruiter_profile.html', context)




@login_required(login_url='login')
def recruiter_login(request):
    """
    The routing logic for when someone clicks on recruiter
    """
    context = {}
    if request.user.is_authenticated:
        is_recruiter = request.user.is_recruiter
        company = request.user.company
        designation = request.user.designation

    if (company is None) or (designation is None):
        return redirect('recruiter_profile')
    else:
        return redirect('recruiter_home')



    context['is_recruiter'] = is_recruiter
    context['company'] = company
    context['designation'] = designation



@login_required(login_url='login')
def recruiter_home(request):
    """
    The homepage of a recruiter - post jobs, track jobs, search for users
    """

    job_data = JobList.objects.filter(user_by = request.user)
    #it will render the data those are applied for jobs
    applied_candiate_data = AppliedCandiate.objects.filter(job_post_user_info__in = job_data)
    print(applied_candiate_data)
    context = {}
    if request.user.is_authenticated:
        is_recruiter = request.user.is_recruiter
        company = request.user.company
        designation = request.user.designation

    if (company is None) or (designation is None):
        return redirect('recruiter_profile')

    # print(applied_candiate_data[0].job_post_user_info)

    return render(request, 'recruiter_home.html', {'job_data':job_data,'applied_candiate_data':applied_candiate_data})


@login_required(login_url = 'login')
def search_jobseekers(request):
    talent_search = TildehatUser.objects.filter(is_recruiter = False)
    return render(request,'jobseeker.html',{'talent_search':talent_search})


@login_required(login_url = 'login')
def hire_talent(request,id):
    new_talent = TildehatUser.objects.get(id = id)
    recuriter_name = request.user
    job_offer = JobList.objects.filter(user_by = recuriter_name)
    if request.method == 'POST':
        req_job_id = request.POST.get("job_id")
        req_email = request.POST.get("email")
        new_talent_offer = job_offer.get(job_id = req_job_id)
        new_talent_offer.offer_to = req_email
        new_talent_offer.save()
    return render(request, 'hire_talent.html',{'new_talent':new_talent,'job_offer':job_offer})
