from django.db import models

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