from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['first_name', 'last_name', 'email','zip_code' ,'mobile', 'address', 'order_notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),


        }