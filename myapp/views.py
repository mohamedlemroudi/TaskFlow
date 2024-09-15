from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title':title
    })


def about(request):
    username = "Moa"
    return render(request, 'about.html', {
        "username":username 
    })


def hello(request, username):
    return HttpResponse("<h1>Hello %s!</h1>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects':projects
    })


def tasks(request):
    # task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html')