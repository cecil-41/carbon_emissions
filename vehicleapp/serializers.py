from rest_framework import serializers
from rest_framework import serializers
from.models import *

# Make Serializer
class VehicleMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = ['id','name']

# Model Serializer  
class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['id', 'name', 'year']

# Estimate Serializer
class VehicleEstimateSerializer(serializers.ModelSerializer):
    distance_value = serializers.FloatField()
    class Meta:
        model = VehicleEstimate
        fields = ['vehicle_model', 'vehicle_year', 'distance_value', 'distance_unit']

        






