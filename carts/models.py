from django.db import models
from django.conf import settings

# Create your models here.
from products.models import Variation

class CartItem(models.Model):
	cart = models.ForeignKey('Cart')
	item = models.ForeignKey(Variation)
	quantity = models.PositiveIntegerField(default=1)
	#line item total

	def __str__(self):
		return self.item.title

class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	items = models.ManyToManyField(Variation, through = CartItem)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return str(self.id)

	# subtotalprice
	# taxes
	# discounts
	# totalprice