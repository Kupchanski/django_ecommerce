from django.conf import settings
from django.db import models

# Create your models here.
from carts.models import Cart


class UserCheckout(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	email = models.EmailField(unique=True) #--> required


	def __str__(self): 
		return self.email

ADDRESS_TYPES = (
	("billing", "Billing"),
	('shipping', "Shipping"),
	)

class UserAddress(models.Model):
	user = models.ForeignKey(UserCheckout)
	type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
	street = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	country = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=120)


	def __str__(self):
		return self.street

class Order(models.Model):
	cart = models.ForeignKey(Cart)
	user = models.ForeignKey(UserCheckout)
	billing_address = models.ForeignKey(UserAddress, related_name='billing_address')
	shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address')
	shipping_total_price = models.DecimalField(decimal_places=2, max_digits=10, default=5.99)
	order_total = models.DecimalField(decimal_places=2, max_digits=10)

	def __str__(self):
		return (self.cart.id)

	#order_id --> custom_id

