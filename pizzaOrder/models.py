from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid

class PizzaSize(models.Model):
    name = models.CharField(max_length=100, default="Medium")

    def __str__(self):
        return self.name

class CrustType(models.Model):
    name = models.CharField(max_length=100, default="Regular")

    def __str__(self):
        return self.name

class SauceType(models.Model):
    name = models.CharField(max_length=100, default="Tomato")

    def __str__(self):
        return self.name

class CheeseType(models.Model):
    name = models.CharField(max_length=100, default="Mozzarella")

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PizzaOrder(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust = models.ForeignKey(CrustType, on_delete=models.CASCADE)
    sauce = models.ForeignKey(SauceType, on_delete=models.CASCADE)
    cheese = models.ForeignKey(CheeseType, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"Order #{self.id} - {self.size} Pizza"
 
class DeliveryDetail(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    #order = models.OneToOneField(PizzaOrder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    def setExpiryDate(self, month, year):
        month = int(month)
        year = int(year)
        self.card_expiry_date = date(year, month, 1)
    card_cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"Delivery for {self.name}"
