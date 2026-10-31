from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='index'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]