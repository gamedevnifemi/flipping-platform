from django.urls import path
from .views import fetch_products, get_sneakers

urlpatterns = [
    path('fetch-products/', fetch_products, name='fetch-products'),
    path('products/', get_sneakers, name='get-sneakers'),
]