from django.db import models
from rides.models import Ride

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    )
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey('booking.Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} for Booking {self.booking_id}"
