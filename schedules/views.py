from django.shortcuts import render
from django.http import JsonResponse
from .models import Schedule
import json

def create_schedule(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        route = data.get('route')
        time = data.get('time')

        schedule = Schedule(route=route, time=time)
        schedule.save()
        return JsonResponse({"message": "Schedule created successfully."})

def view_schedules(request):
    schedules = Schedule.objects.all()
    return JsonResponse({"schedules": [schedule.route for schedule in schedules]})

# Additional views for listing, updating, and deleting schedules can be added here.
