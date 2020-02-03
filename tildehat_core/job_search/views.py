from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from ..jobpost.models import JobList,AppliedCandiate


import psycopg2 #yeah I know
from tildehat_core.common.utils import normalize_encode_search_query, decode_search_query, binary_to_dict

def open_job_search_page(request, query='job'):
    context = {}
    if request.method == 'POST': # If the form is submitted
        search_query = normalize_encode_search_query(request.POST.get('search-box', None))
        return redirect('/job_search/?q=' + search_query) #The '/' is super important for this relative path to work
    if request.method == 'GET':
        query = str(request.GET.get('q', 'job')) # "job" is a catch-all if we are unable to get ?q, in case someone opens /job_search/ there is something to show
    decoded_query = decode_search_query(query)
    # context['search_term'] = query # debug the decoded query


    # A postgres transaction, put entire thing in try/catch
    try:
        cur.close()
    except:
        pass
    try:
        conn.close()
    except:
        pass

    conn = psycopg2.connect(
                user="postgres",
                password="12345678",
                host="jd.cdxojf43tdux.ap-south-1.rds.amazonaws.com",
                port='5432'
            )
    cur = conn.cursor()

    # TODO
    # SQL injection protection here
    # Handle weird queries and improve search/ranking in general





    cur.execute("""SELECT post,date,phone_number,valid_jd, enrichment, ts_rank(tsv, plainto_tsquery('english','"""+decoded_query+"""')) as rank_score
    FROM unstructured_jd, to_tsquery('english', '"""+'|'.join(decoded_query.split())+"""') AS q
    WHERE (tsv @@ q) and valid_jd=True ORDER BY rank_score LIMIT 100""")

    context['query'] = """SELECT post,date,phone_number,valid_jd, enrichment, ts_rank(tsv, plainto_tsquery('english','"""+decoded_query+"""')) as rank_score
    FROM unstructured_jd, to_tsquery('english', '"""+'|'.join(decoded_query.split())+"""') AS q
    WHERE (tsv @@ q) and valid_jd=True ORDER BY rank_score LIMIT 100"""

    keys = ['post', 'date', 'number', 'valid_jd', 'enrichment', 'rank']

    context['jobs'] = [dict(zip(keys, i)) for i in list(cur.fetchall())]

    job_data = JobList.objects.all()

    c = 0

    for i in context['jobs']:
        i['post'] = i['post'].replace('\n', '<br>')
        i['enrichment'] = eval(str(binary_to_dict(i['enrichment'])))
        i['count'] = str(c)
        c+=1


    for j in range(0,len(job_data)):
        context['jobs'].append(
            {
                'post':job_data[j].job_description,
                'job_id':job_data[j].job_id,
                'date':job_data[j].date,
                'number':'+91 70076 68212',
                'valid_jd':True,
                'enrichment': {'role': job_data[j].job_description, 'company': 'mnc', 'city': 'City near you',
                              'salary': 'Industry Standards', 'openings': -1, 'education': 'Diploma',
                              'skills': ['Excellent Commincation Skills / Quick Learner'],
                              'experience': '(Fresher or Experienced)'},
                'rank': 0.0607927,
            }
        )
        c+=1

    # for data in context['jobs']:
    #     print(data)



        # print(i['post'])
        #print (i) get all keys in i
        #jd, date - rest random
    # for job in fetched_jobs:
    #     context[jobs].append({'post':job.post})

    # for data in context:
    #     print(data.add)
    # print("jobs:",context['jobs'][0])
    cur.close()
    conn.close()
    return render(request,'job_search.html', context)

@login_required(login_url='login')
def job_apply(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            req_candiate_email = request.POST.get("candiate_email")
            req_job_id = request.POST.get("job_id")
            if req_job_id is "":
                req_job_id = 0
            try:
                job_post_data = JobList.objects.get(job_id = req_job_id)
            except JobList.DoesNotExist:
                pass

            AppliedCandiate.objects.create(job_post_user_info = job_post_data,student_details = req_candiate_email)

        else:
            return redirect("login")
    return render(request,'applied_successfully.html')
