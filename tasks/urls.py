from django.urls import path
from . import views

urlpatterns = [
    # This maps the /api/tasks URL to the add_new_task view
    path('tasks', views.add_new_task, name='add_new_task'),
]