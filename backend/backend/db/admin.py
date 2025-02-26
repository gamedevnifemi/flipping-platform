from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Product

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'github_id', 'is_active_user']

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'marketplace', 'date_fetched')
    search_fields = ('title', 'marketplace')

