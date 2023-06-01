from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ('email', 'username')


admin.site.register(CustomUser, CustomUserAdmin)