from django.urls import path
from .views import register_user, login_user, homepage, customer_dashboard, logout_user
from rides.views import check_shuttle_availability, book_ride  # Import the new function
from .admin_views import admin_dashboard  # Ensure this is imported

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register_user, name='register'),
    path('signup/', register_user, name='signup'),
    path('login/', login_user, name='login'),
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    path('logout/', logout_user, name='logout'),
    path('book_a_ride/', book_ride, name='book_a_ride'),  # Updated to use book_ride
    path('check_availability/', check_shuttle_availability, name='check_shuttle_availability'),  # Updated URL pattern
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),  # Corrected line
]
