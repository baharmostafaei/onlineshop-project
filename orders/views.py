from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required

@login_required
def order_create_view(request):
    order_form = forms.OrderForm()
    if request.method == 'POST':
        order_form = forms.OrderForm(request.POST, )
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            
    
    return render(request, 'orders/order_create.html', {
        'form': order_form
    })