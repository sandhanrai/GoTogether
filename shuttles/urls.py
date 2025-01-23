from django.urls import path
from .views import create_shuttle, view_shuttles  # Import your views here

urlpatterns = [
    path('create/', create_shuttle, name='create_shuttle'),  # Example URL pattern
    path('view/', view_shuttles, name='view_shuttles'),  # Example URL pattern
]
