from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Product, Orders, Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Cart)