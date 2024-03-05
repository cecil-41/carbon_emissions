from django.urls import path, include
from rest_framework_nested import routers
from . import views

# URLconf
# Routers
router = routers.DefaultRouter()
router.register('models', views.VehicleModelView, basename='models')

# Nested routers
model_router = routers.NestedDefaultRouter(router, 'models', lookup='model')
model_router.register('estimates', views.VehicleEstimateView, basename='make-estimates')


urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('profile/', views.profilePage, name='profile'),
]
