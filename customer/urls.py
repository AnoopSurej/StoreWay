from django.urls import path, include
from . import views

urlpatterns = [
    path('cdashboard', views.customer_dashboard, name='customer-dashboard'),
]
