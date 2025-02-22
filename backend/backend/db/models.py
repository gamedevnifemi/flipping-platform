from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    marketplace = models.CharField(max_length=50, choices=[("eBay", "eBay"), ("StockX", "StockX")])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
