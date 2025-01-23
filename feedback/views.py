from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback

def submit_feedback(request):
    # Logic for submitting feedback
    return JsonResponse({"message": "Feedback submitted successfully."})
