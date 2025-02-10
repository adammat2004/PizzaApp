from django.contrib import admin
from .models import PizzaSize, CrustType, SauceType, CheeseType, Topping

# Register your models here.
admin.site.register(PizzaSize)
admin.site.register(CrustType)
admin.site.register(SauceType)
admin.site.register(CheeseType)
admin.site.register(Topping)