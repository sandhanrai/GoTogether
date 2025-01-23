from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        user_type = request.POST.get('user-type').lower()

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return render(request, 'signup.html')

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format.")
            return render(request, 'signup.html')

        # Validate phone number (example: must be 10 digits)
        if not re.match(r'^\d{10}$', phone_number):
            messages.error(request, "Phone number must be 10 digits.")
            return render(request, 'signup.html')

        # Check password strength
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number, role=user_type)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        
        if user_type == 'customer':
            return redirect('customer_dashboard')
        elif user_type == 'driver':
            return redirect('driver_dashboard')

    return render(request, 'signup.html')

def customer_dashboard(request):
    username = request.user.username  # Get the logged-in user's username
    return render(request, 'customer_dashboard.html', {'username': username})  # Pass the username to the template

def driver_dashboard(request):
    return render(request, 'driver_dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')

def login_user(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone_number=identifier)
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return render(request, 'login.html')

        if user.check_password(password):
            if user.role == 'customer':
                return redirect('customer_dashboard')
            elif user.role == 'driver':
                return redirect('driver_dashboard')
        else:
            messages.error(request, "Invalid password.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def check_availability(request):
    return render(request, 'check_availability.html')

def homepage(request):
    return render(request, 'homepage.html')
