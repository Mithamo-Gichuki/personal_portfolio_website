from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_home, name='projects_home'),
    path('<int:projects_id>/', views.project_details, name='project_details'),
    path('trial', views.trial, name='trial'),
    
]