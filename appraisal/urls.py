"""ExpertAutoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from .views import ( ManufacturerCreateView, ManufacturerDeleteView, ManufacturerDetailView, ManufacturerListView, ManufacturerUpdateView, VehicleCreateView, VehicleDeleteView, VehicleDetailView, VehicleListView, VehicleUpdateView )
from appraisal import views

urlpatterns = [
    path('add-vehicle', VehicleCreateView.as_view(), name='vehicle_new'),
    path('vehicle/<int:pk>', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('edit-vehicle/<int:pk>', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('delete-vehicle/<int:pk>', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicles', views.filter_vehicles, name='vehicle_list'),
    path('', views.dashboard, name="dashboard"),
    path('add-manufacturer', ManufacturerCreateView.as_view(), name="manufacturer_new"),
    path('edit-manufacturer/<int:pk>', ManufacturerUpdateView.as_view(), name="manufacturer_update"),
    path('manufacturer/<int:pk>', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturers', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('delete-manufacturer/<int:pk>', ManufacturerDeleteView.as_view(), name='manufacturer_delete'),




]
