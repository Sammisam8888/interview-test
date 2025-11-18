from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    # We include the URLs from our 'tasks' app
    path('api/', include('tasks.urls')),
    
    # A simple index route
    path('', lambda r: JsonResponse({"message": "Interview API is running. Please use the /api/tasks endpoint."})),
]