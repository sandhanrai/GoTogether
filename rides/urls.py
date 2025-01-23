from django.urls import path
from .views import create_ride, book_ride, check_shuttle_availability, create_shuttle, create_schedule

urlpatterns = [
    path('create/', create_ride, name='create_ride'),
    path('book/', book_ride, name='book_ride'),
    path('check_availability/', check_shuttle_availability, name='check_shuttle_availability'),
    path('create_shuttle/', create_shuttle, name='create_shuttle'),
    path('create_schedule/', create_schedule, name='create_schedule'),
]
