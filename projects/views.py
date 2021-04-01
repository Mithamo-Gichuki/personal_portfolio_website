from django.shortcuts import render, get_object_or_404
from .models import Projects


# Create your views here.


def projects_home(request):
    # This shows all projects
    # projects = Projects.objects.all()
    projects = Projects.objects.order_by('-date')  # [:1]  # -date shows latest first [:1] shows last 1
    return render(request, 'projects/projects_home.html', {'projects': projects})


def project_details(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'projects/project_details.html', {'project': project})

def trial(request):
	projects = Projects.objects.order_by('-date')
	return render(request, 'projects/trial.html', {'projects' : projects})