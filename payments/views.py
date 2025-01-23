from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment

def process_payment(request):
    # Logic for processing a payment
    return JsonResponse({"message": "Payment processed successfully."})
