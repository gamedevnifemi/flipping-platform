from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'github_id', 'is_active_user']

admin.site.register(CustomUser, CustomUserAdmin)
