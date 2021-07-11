from django.db import models
from django.db.models import Model
from users.models import StoreWayUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Shops(models.Model):
	shopkeeper_email = models.EmailField(primary_key=True) 
	shop_name = models.CharField(max_length=40)
	shop_type = models.CharField(max_length=20)
	address = models.TextField()
	district = models.CharField(max_length=25)
	localbody = models.CharField(max_length=25)
	wardnum = models.IntegerField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()
	q_slot_time = models.IntegerField()
	q_slot_capacity = models.IntegerField()
	description = models.TextField()

class ShopRegistry(models.Model):
	shopkeeper_email = models.EmailField()
	customerFirstName = models.CharField(max_length=20)
	customerLastName = models.CharField(max_length=20)
	customerPhone = models.CharField(max_length=10)
	dateEntry = models.DateTimeField()
	queueTimeSlot = models.TimeField()
	shopEnterTime = models.TimeField(auto_now=True)

class ContainmentZone(models.Model):
	district = models.CharField(max_length=30)
	localbody = models.CharField(max_length=30)
	wardnum = models.IntegerField()

class ShopItems(models.Model):
	shopkeeper_email = models.EmailField()
	item_name=models.CharField(max_length=120)
	item_price=models.FloatField()
	item_quantity=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])
	item_description=models.TextField(blank=True)

	def __str__(self):
		return self.shopkeeper_email