from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Flight(models.Model):
    flight_name = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    seats = models.JSONField(default=list)

    def __str__(self):
        return f"Flight {self.flight_name}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Populate seats with 50 empty seats
            self.seats = [-1] * 50
        super().save(*args, **kwargs)
