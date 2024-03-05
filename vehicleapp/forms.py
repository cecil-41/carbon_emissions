from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import VehicleModel 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class EmissionForm(forms.Form):
    vehicle_model = forms.ModelChoiceField(
        queryset=VehicleModel.objects.filter(vehicle_make__name='Toyota'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )
    year = forms.ChoiceField(
        choices=[(year, year) for year in range(1950, 2025)],
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )
    measure_units = forms.ChoiceField(
        choices=[('G', 'Grams'), ('LB', 'Pounds'), ('KG', 'Kilograms'), ('MT', 'Megatons')],
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )


