from django.contrib import admin
from .models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Comment)