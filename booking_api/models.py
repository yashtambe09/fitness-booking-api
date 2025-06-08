from django.db import models
from django.utils import timezone

# Create your models here.

class FitnessClass(models.Model):
    CLASS_TYPES = [
        ("Yoga", "Yoga"),
        ("Zumba", "Zumba"),
        ("HIIT", "HIIT"),
    ]
    name = models.CharField(max_length=50, choices=CLASS_TYPES)
    datetime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} with {self.instructor} at {self.datetime}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name} ({self.client_email})"
