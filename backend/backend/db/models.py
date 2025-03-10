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
    PLATFORM_CHOICES = [
        ('ebay', 'eBay'),
        ('stockx', 'StockX'),
        ('goat', 'GOAT'),
        ('amazon', 'Amazon'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=255, blank=True, null=True)
    marketplace = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    date_fetched = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()
    product_url = models.URLField()

    def __str__(self):
        return f"{self.title} - {self.marketplace} - £{self.price}"

class Sneaker(models.Model):
    style_id = models.CharField(max_length=50, unique=True)
    shoe_name = models.CharField(max_length=255)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    thumbnail = models.URLField()
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    colorway = models.CharField(max_length=100, null=True, blank=True)
    stockx_url = models.URLField()
    goat_url = models.URLField()
    date_released = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shoe_name} - {self.style_id}"

class SneakerPriceHistory(models.Model):
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE, related_name="price_history")
    recorded_at = models.DateTimeField(auto_now_add=True)
    stockx_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    goat_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.sneaker.shoe_name} - {self.recorded_at.strftime('%Y-%m-%d')}"

