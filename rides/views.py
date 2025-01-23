from django.shortcuts import render
from django.http import JsonResponse
from .models import Ride, Shuttle, Schedule
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

# Existing ride-related views...

def create_shuttle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        vehicle_number = data.get('vehicle_number')
        capacity = data.get('capacity')

        shuttle = Shuttle(vehicle_number=vehicle_number, capacity=capacity)
        shuttle.save()
        return JsonResponse({"message": "Shuttle created successfully."})

def create_schedule(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        route = data.get('route')
        shuttle_id = data.get('shuttle_id')
        time_slot = data.get('time_slot')

        schedule = Schedule(route=route, shuttle_id=shuttle_id, time_slot=time_slot)
        schedule.save()
        return JsonResponse({"message": "Schedule created successfully."})

def create_ride(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rider_id = data.get('rider_id')
        driver_id = data.get('driver_id')
        pickup_point = data.get('pickup_point')
        dropoff_point = data.get('dropoff_point')
        scheduled_time = data.get('scheduled_time')
        status = data.get('status', 'Pending')  # Default status

        ride = Ride(
            rider_id=rider_id,
            driver_id=driver_id,
            pickup_point=pickup_point,
            dropoff_point=dropoff_point,
            scheduled_time=scheduled_time,
            status=status
        )
        ride.save()
        return JsonResponse({"message": "Ride created successfully."})

def check_shuttle_availability(request):
    # Logic to check shuttle availability
    available_shuttles = Shuttle.objects.all()  # Example logic
    return JsonResponse({"available_shuttles": [shuttle.vehicle_number for shuttle in available_shuttles]})

def book_ride(request):
    return render(request, 'book_a_ride.html')  # Render the booking page

# Additional views for listing, updating, and deleting shuttles and schedules can be added here.
