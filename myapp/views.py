from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Views for the application

def index(request):
    """
    Render the homepage with a title.
    """
    return render(request, 'index.html', {
        'title': 'Django Course!'
    })

def about(request):
    """
    Render the 'About' page with a sample username.
    """
    return render(request, 'about.html', {
        'username': 'Moa'
    })

def projects(request):
    """
    Fetch all projects and render them on the 'projects' page.
    """
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    """
    Fetch all tasks and render them on the 'tasks' page.
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    """
    Handle task creation. 
    Display the form on GET requests and save the task on POST requests.
    """
    if request.method == 'GET':
        # Render the form to create a new task
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    elif request.method == 'POST':
        # Create a new task with the form data
        Task.objects.create(
            title=request.POST['title'], 
            description=request.POST['description'], 
            project_id=2  # Note: this is hardcoded for now, consider improving
        )
        return redirect('tasks')

def create_project(request):
    """
    Handle project creation. 
    Display the form on GET requests and save the project on POST requests.
    """
    if request.method == 'GET':
        # Render the form to create a new project
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    elif request.method == 'POST':
        # Create a new project with the form data
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    """
    Display the details of a single project including its tasks.
    """
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
