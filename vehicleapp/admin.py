from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    # Actions
    list_display=['id','name', 'number_of_models']
    # filtering
    ordering=['name']
    list_per_page = 10
    # Optimizing queries
    search_fields=['name__istartswith']

@admin.register(models.VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['id','vehicle_make', 'name', 'year']
    search_fields = ['vehicle_make', 'name']
    # list_filter = ['vehicle_make', 'name']
    list_select_related = ['vehicle_make']
    autocomplete_fields=['vehicle_make']
    list_per_page = 10

@admin.register(models.VehicleEstimate)
class VehicleEstimateAdmin(admin.ModelAdmin):
    list_display = ('vehicle_make', 'vehicle_model', 'distance_value', 'distance_unit', 'carbon_g', 'carbon_lb', 'carbon_kg', 'carbon_mt', 'estimated_at')
    search_fields = ['vehicle_make', 'vehicle_model', 'vehicle_year']
    # list_filter = ['vehicle_make', 'vehicle_model']
    list_select_related = ['vehicle_make', 'vehicle_model']
    autocomplete_fields=['vehicle_make', 'vehicle_model']
