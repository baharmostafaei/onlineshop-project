from django.contrib import admin
from .models import Order, OrederItem

class OrederItemInLine(admin.TabularInline):
    model = OrederItem
    fields = ['order', 'product', 'quantity', 'price',]
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile','address', 'order_notes', 'is_paid']
    inlines =[
        OrederItemInLine,
    ]

@admin.register(OrederItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price',]
    
