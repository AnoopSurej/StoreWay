from django.contrib import admin
from .models import OrderHistory,DeliveryAddress

admin.site.register(OrderHistory)
admin.site.register(DeliveryAddress)

# Register your models here.
