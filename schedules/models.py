from django.db import models
from shuttles.models import Shuttle

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    route = models.CharField(max_length=255, null=False)
    shuttle_id = models.ForeignKey(Shuttle, on_delete=models.CASCADE)
    time_slot = models.DateTimeField(null=False)

    def __str__(self):
        return f"Schedule {self.schedule_id} for {self.route} at {self.time_slot}"
