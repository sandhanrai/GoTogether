from django.urls import path
from .views import create_schedule, view_schedules  # Import your views here

urlpatterns = [
    path('create/', create_schedule, name='create_schedule'),  # Example URL pattern
    path('view/', view_schedules, name='view_schedules'),  # Example URL pattern
]
