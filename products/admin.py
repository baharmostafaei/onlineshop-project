from django.contrib import admin
from .models import Product, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_created',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('product','body' ,'active',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)