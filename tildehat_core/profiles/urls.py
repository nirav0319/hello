
# django
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

# app
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page ='chat_agent'), name= 'logout'),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter_profile/', views.recruiter_profile, name='recruiter_profile'),
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('jobseekers/', views.search_jobseekers, name='job_seekers'),
    path('hire/<int:id>/', views.hire_talent, name='hire_talent'),
]
