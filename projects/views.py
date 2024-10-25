from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# projectsList = [
#   {
#     "id": "1",
#     "title": "DevBlog",
#     "description": "A developer's blog platform with Markdown support and live previews"
#   },
#   {
#     "id": "2",
#     "title": "Portfolio Showcase",
#     "description": "A personal portfolio project to showcase my skills and projects"
#   },
#   {
#     "id": "3",
#     "title": "Social Network",
#     "description": "Awesome open source project I am still working on"
#   },
#   {
#     "id": "4",
#     "title": "Task Manager",
#     "description": "A simple and effective task management tool for personal use"
#   },
#   {
#     "id": "5",
#     "title": "Weather App",
#     "description": "An app to track weather using open APIs and display forecasts"
#   },
#   {
#     "id": "6",
#     "title": "E-commerce Platform",
#     "description": "A full-fledged e-commerce website with payment gateway integration"
#   },
#   {
#     "id": "7",
#     "title": "Fitness Tracker",
#     "description": "An app to monitor fitness progress and log workout routines"
#   },
#   {
#     "id": "8",
#     "title": "Chat Application",
#     "description": "A real-time chat application with support for groups and media sharing"
#   },
#   {
#     "id": "9",
#     "title": "Recipe Finder",
#     "description": "An app to search for recipes by ingredients and dietary preferences"
#   },
#   {
#     "id": "10",
#     "title": "Travel Planner",
#     "description": "A travel itinerary planner with accommodation and activity suggestions"
#   },
#   {
#     "id": "11",
#     "title": "Photo Gallery",
#     "description": "A digital photo gallery for organizing and sharing images online"
#   }
# ]


def projects(request):
    projects = Project.objects.all()
    project_fields = Project._meta.fields  # This gets all the model fields

    return render(request, 'projects/projects.html',{"projects":projects,"project_fields":project_fields})

def project(request,pk):
  project = Project.objects.get(id=pk)
  tags = project.tags.all()
  
  return render(request,'projects/single-project.html',{"project":project,"tags":tags})

  











    # projectObj = None
    # for i in projectsList:
    #     if i["id"]==pk:
    #         projectObj = i
    # return render(request,'projects/single-project.html',{"project":projectObj})
  