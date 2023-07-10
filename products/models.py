from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='product/product_cover', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),        
        ('2', _('Bad')),
        ('3', _('Good')),
        ('4', _('Very Good')),
        ('5', _('Amazing')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name=_('Comment\'s text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Your Rate'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
     
    # Manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentManager()
 

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
    
    


    
