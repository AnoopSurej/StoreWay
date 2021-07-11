from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CustomerQueue(models.Model):
	shopkeeper_email = models.EmailField()
	shop_name = models.CharField(max_length=30)
	shopkeeper_phone = models.CharField(max_length=10)
	customerFirstName = models.CharField(max_length=30)
	customerLastName = models.CharField(max_length=30)
	customerEmail =  models.EmailField()
	customerPhone = models.CharField(max_length=10)
	queueEnterTime = models.DateTimeField(auto_now=True)
	queueTimeSlot = models.TimeField()

class CovidAlert(models.Model):
	shop_name = models.CharField(max_length=30)
	customerEmail = models.EmailField()
	is_read = models.BooleanField(default=False)
	date = models.DateTimeField()
	time = models.TimeField(auto_now=True)

class OrderHistory(models.Model):
	customerEmail =  models.EmailField()
	customerFirstName = models.CharField(max_length=30)
	customerLastName = models.CharField(max_length=30)
	shopkeeper_email = models.EmailField()
	shop_name = models.CharField(max_length=30)
	item_name=models.CharField(max_length=120)
	item_price=models.FloatField()
	currentdate= models.DateTimeField()
	

	def __str__(self):
		return self.customerEmail

class DeliveryAddress(models.Model):
	customerEmail =  models.EmailField()
	delivery_address=models.TextField()
	delivery_pin=models.IntegerField()
	delivery_district=models.CharField(max_length=20)

	def __str__(self):
		return self.customerEmail