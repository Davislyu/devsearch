from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    project_fields = Project._meta.fields  # This gets all the model fields

    return render(
        request,
        "projects/projects.html",
        {"projects": projects, "project_fields": project_fields},
    )


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()

    return render(
        request, "projects/single-project.html", {"project": project, "tags": tags}
    )


def createProject(request):
    form = ProjectForm()
    content = {"form": form}
    return render(request, "projects/project_form.html", content)
