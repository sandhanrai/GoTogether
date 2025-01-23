from django.db import models
from rides.models import Ride
from users.models import User

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    payment_status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ])

    def __str__(self):
        return f"Booking {self.booking_id} for Ride {self.ride.ride_id}"
