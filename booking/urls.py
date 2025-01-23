from django.urls import path
from .views import create_booking, view_bookings  # Import your views here

urlpatterns = [
    path('create/', create_booking, name='create_booking'),  # Example URL pattern
    path('view/', view_bookings, name='view_bookings'),  # Example URL pattern
]
