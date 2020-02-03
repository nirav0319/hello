# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse

from tildehat_core.common.utils import normalize_encode_search_query

def open_chat_agent_page(request):
    if request.method == 'POST': # If the form is submitted
        search_query = normalize_encode_search_query(request.POST.get('search-box', None))
        return redirect('job_search/?q=' + search_query)
    else:
        return render(request, 'chat_agent.html')


def open_about_page(request):
    return render(request, 'about.html')