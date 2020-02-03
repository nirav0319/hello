# django
from django.urls import path

# app
from . import views

urlpatterns = [
    path('', views.open_chat_agent_page, name='chat_agent'),
    path('about/', views.open_about_page, name='about'),
]
