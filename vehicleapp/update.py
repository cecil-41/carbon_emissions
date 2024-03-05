from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
import requests
from .models import VehicleMake, VehicleModel, VehicleEstimate

class VehicleMakeAPIView(APIView):
    def get(self, request):
        # Make a request to the Carbon Emission API to get vehicle makes
        response = requests.get('https://www.carboninterface.com/api/v1/vehicle_makes', headers={'Authorization': 'Bearer GWilh514kupPskObRuWtEA'})
        data = response.json()

        # Loop through the data and create or update VehicleMake objects in the database
        for item in data:
            vehicle_make, created = VehicleMake.objects.get_or_create(
                id=item['data']['id'],
                name=item['data']['attributes']['name'],
                number_of_models=item['data']['attributes']['number_of_models']
            )

        # Return the vehicle makes as JSON
        return Response(data, status=status.HTTP_200_OK)
    
class VehicleModelAPIView(APIView):
    def get(self, request, vehicle_make_id):
        # Make a request to the Carbon Emission API to get vehicle models for a specific vehicle make
        response = requests.get(f'https://www.carboninterface.com/api/v1/vehicle_makes/{vehicle_make_id}/vehicle_models', headers={'Authorization': 'Bearer GWilh514kupPskObRuWtEA'})
        data = response.json()

        # Loop through the data and create or update VehicleModel objects in the database
        for item in data:
            vehicle_model, created = VehicleModel.objects.get_or_create(
                id=item['data']['id'],
                name=item['data']['attributes']['name'],
                year=item['data']['attributes']['year'],
                vehicle_make_id=vehicle_make_id
            )

        # Return the vehicle models as JSON
        return Response(data, status=status.HTTP_200_OK)

class VehicleEstimateAPIView(APIView):
    def post(self, request):
        # Extract data from the request
        data = request.data

        # Make a request to the Carbon Emission API to get vehicle estimates
        response = requests.post('https://www.carboninterface.com/api/v1/estimates', headers={'Authorization': 'Bearer GWilh514kupPskObRuWtEA'}, json=data)
        response_data = response.json()

        # Create or update VehicleEstimate object in the database
        vehicle_estimate, created = VehicleEstimate.objects.get_or_create(
            id=response_data['data']['id'],
            vehicle_make=response_data['data']['attributes']['vehicle_make'],
            vehicle_model=response_data['data']['attributes']['vehicle_model'],
            vehicle_year=response_data['data']['attributes']['vehicle_year'],
            distance_value=response_data['data']['attributes']['distance_value'],
            distance_unit=response_data['data']['attributes']['distance_unit'],
            carbon_g=response_data['data']['attributes']['carbon_g'],
            carbon_lb=response_data['data']['attributes']['carbon_lb'],
            carbon_kg=response_data['data']['attributes']['carbon_kg'],
            carbon_mt=response_data['data']['attributes']['carbon_mt'],
            estimated_at=response_data['data']['attributes']['estimated_at']
        )

        # Return the vehicle estimate as JSON
        return Response(response_data, status=status.HTTP_200_OK)