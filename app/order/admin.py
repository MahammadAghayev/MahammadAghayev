from django.contrib import admin

from .models import Order, WishList
# Register your models here.


admin.site.register(Order)
admin.site.register(WishList)