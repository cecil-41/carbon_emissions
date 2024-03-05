from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from vehicleapp.models import *
import requests
from  vehicleapp.serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class VehicleMakeView(ModelViewSet):
    queryset = VehicleMake.objects.all()
    serializer_class = VehicleMakeSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return [IsAuthenticated()]
        return [IsAdminUser()]

class VehicleModelView(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return [IsAuthenticated()]
        return [IsAdminUser()]
    
    

class VehicleEstimateView(ModelViewSet):
    serializer_class = VehicleEstimateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.kwargs)
        return VehicleEstimate.objects.filter(vehicle_model_id=self.kwargs['model_pk'])
    
    def get_serializer_context(self):
        return {'vehicle_model_id': self.kwargs['model_pk']}

    def create(self, request, *args, **kwargs):
        # Validate the request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the validated data
        validated_data = serializer.validated_data

        # Make a request to the Carbon Emission API
        url = "https://www.carboninterface.com/api/v1/estimates"
        headers = {
            "Authorization": "Bearer GWilh514kupPskObRuWtEA",
            "Content-Type": "application/json"
        }
        data = {
            "type": "vehicle",
            "distance_unit": validated_data["distance_unit"],
            "distance_value": validated_data["distance_value"],
            "vehicle_model_id": validated_data["vehicle_model"].id

        }

        response = requests.post(url, headers=headers, json=data)

        # Return the estimates to the user
        return Response(response.json(), status=status.HTTP_200_OK)

