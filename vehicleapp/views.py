from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .forms import CreateUserForm, LoginForm, ProfileForm, EmissionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse


# Index View
def homePage(request):
    if(request.user.is_authenticated):
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.warning(request, 'Invalid credentials!')
        else:
            form = LoginForm()

        context = {'form': form}
        return render(request, 'login.html', context)

# Register View
def registerPage(request):
    if(request.user.is_authenticated):
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')

                return redirect('login')  # Redirect to the login page after successful registration
            else:
                # If the form data is not valid, render the form again with the errors
                return render(request, 'register.html', {'form': form})

        context = {'form': form}
        return render(request, 'register.html', context)

# Login View
def loginPage(request):
    if(request.user.is_authenticated):
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.warning(request, 'Invalid credentials!')
        else:
            form = LoginForm()

        context = {'form': form}
        return render(request, 'login.html', context)

# Dashboard View
@login_required(login_url='login')
def dashboardPage(request):
    context= {}
    return render(request, 'dashboard.html',context)

# Profile View
@login_required(login_url='login')
def profilePage(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Details updated!')
            return redirect('profile')

    else:
        form = ProfileForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)

# Logout View
def logoutPage(request):
    logout(request)
    return redirect('login')

def calculate_emissions(request):
    form = EmissionForm()
    context = {'form': form}

    return render(request, 'dashboard.html', context)







    
    
    