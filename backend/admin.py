from django.contrib import admin
from backend.models import CustomUserModel
from backend.forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    model = CustomUserModel



admin.site.register(CustomUserModel, CustomUserAdmin)