from django.shortcuts import render
from django.http import JsonResponse
from .models import Shuttle
import json

def create_shuttle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        vehicle_number = data.get('vehicle_number')
        capacity = data.get('capacity')

        shuttle = Shuttle(vehicle_number=vehicle_number, capacity=capacity)
        shuttle.save()
        return JsonResponse({"message": "Shuttle created successfully."})

def view_shuttles(request):
    shuttles = Shuttle.objects.all()
    return JsonResponse({"shuttles": [shuttle.vehicle_number for shuttle in shuttles]})

# Additional views for listing, updating, and deleting shuttles can be added here.
