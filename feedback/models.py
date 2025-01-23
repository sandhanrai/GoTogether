from django.db import models
from users.models import User
from rides.models import Ride

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Feedback {self.feedback_id} by {self.user.name} for Ride {self.ride.ride_id}"
