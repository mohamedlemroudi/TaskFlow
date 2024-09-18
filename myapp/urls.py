from django.urls import path  # Import the 'path' function to define routes
from . import views           # Import views from the views.py file

# Define the URLs and associate each one with its corresponding view
urlpatterns = [
    path('', views.index, name="index"),  # Main route, associated with the 'index' view
    path('about/', views.about, name="about"),  # Route for the 'about' page
    path('projects/', views.projects, name="projects"),  # Displays all projects
    path('projects/<int:id>/', views.project_detail, name="project_detail"),  # Route for the details of a specific project
    path('tasks/', views.tasks_list, name="tasks_list"),  # Displays all tasks
    path('tasks/mark_done/<int:task_id>/', views.mark_task_done, name='mark_task_done'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('create_task/', views.create_task, name="create_task"),  # Route to create a new task
    path('create_project/', views.create_project, name="create_project"),  # Route to create a new project
]
