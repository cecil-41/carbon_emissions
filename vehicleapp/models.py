from django.db import models
# Create your models here.
from django.db import models

class VehicleMake(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    number_of_models = models.IntegerField()

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    vehicle_make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_make.name} {self.name} ({self.year})"

class VehicleEstimate(models.Model):
    DISTANCE_UNIT_CHOICES = [
        ('mi', 'miles'),
        ('km', 'kilometers'),
    ]
    vehicle_make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    vehicle_year = models.IntegerField()
    distance_value = models.DecimalField(max_digits=10, decimal_places=2)
    distance_unit = models.CharField(max_length=20, choices=DISTANCE_UNIT_CHOICES)
    carbon_g = models.DecimalField(max_digits=10, decimal_places=2)
    carbon_lb = models.DecimalField(max_digits=10, decimal_places=2)
    carbon_kg = models.DecimalField(max_digits=10, decimal_places=2)
    carbon_mt = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_make.name} {self.vehicle_model.name} ({self.vehicle_year})"
