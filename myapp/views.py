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

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def mark_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return redirect('tasks_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks_list')

def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            project = form.cleaned_data['project']

            # Crear la tarea
            Task.objects.create(title=title, description=description, project=project)

            return redirect('tasks_list')  # Redirige a una vista de lista de tareas o similar
    else:
        form = CreateNewTask()
    
    return render(request, 'tasks/create_task.html', {'form': form})



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
