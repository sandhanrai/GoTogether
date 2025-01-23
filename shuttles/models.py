from django.db import models

class Shuttle(models.Model):
    shuttle_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField(null=False)

    def __str__(self):
        return f"Shuttle {self.vehicle_number} with capacity {self.capacity}"
