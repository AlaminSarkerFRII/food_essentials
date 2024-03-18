from django.contrib import admin
from .models import CartItem, Products,Customer
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'description', 'category',
                    'discount_prices', 'product_image']


admin.site.register(Products, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'identity', 'mobile',
                    'state']


admin.site.register(Customer, CustomerAdmin)


class CartItemAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'user', 'products', 'quantity']
    readonly_fields = ['user',]
    
    
admin.site.register(CartItem, CartItemAdmin)
