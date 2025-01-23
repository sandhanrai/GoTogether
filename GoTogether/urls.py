from django.contrib import admin
from django.urls import path, include
from users.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),  # Redirect root URL to homepage
    path('users/', include('users.urls')),  # Corrected syntax
    path('rides/', include('rides.urls')),  # Corrected syntax
    path('booking/', include('booking.urls')),  # Corrected syntax
    path('payments/', include('payments.urls')),
    path('feedback/', include('feedback.urls')),
    path('schedules/', include('schedules.urls')),  # Corrected syntax
    path('shuttles/', include('shuttles.urls')),  # Corrected syntax
]
