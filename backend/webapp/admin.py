from django.contrib import admin
from .models import Product, productType, provider, Cart, CartItem
# Register your models here.

admin.site.register([Product, productType, provider, Cart, CartItem])