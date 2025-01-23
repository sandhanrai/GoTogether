from django.db import models
from users.models import User

class Ride(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    ride_id = models.AutoField(primary_key=True)
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_point = models.CharField(max_length=255)
    dropoff_point = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Ride {self.ride_id} from {self.pickup_point} to {self.dropoff_point}"

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return f"Schedule {self.schedule_id} for route {self.route}"

class Shuttle(models.Model):
    shuttle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Shuttle {self.vehicle_number} with capacity {self.capacity}"
