from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User model for extended user attributes"""
    email = models.EmailField(blank=True, null=True)  # Make email optional
    github_id = models.CharField(max_length=50, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    is_active_user = models.BooleanField(default=True)  # Track active users
    
    class Meta:
        db_table = 'db_customuser'

    def __str__(self):
        return self.username



class Product(models.Model):
    name = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=50, choices=[("eBay", "eBay"), ("StockX", "StockX")])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
