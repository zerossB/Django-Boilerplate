from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "name", "is_active")
