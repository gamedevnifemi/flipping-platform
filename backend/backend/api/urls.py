from django.urls import path
from .views import fetch_products, get_sneakers, get_price_history

urlpatterns = [
    path('fetch-products/', fetch_products, name='fetch-products'),
    path('products/', get_sneakers, name='get-sneakers'),
        # Price Trends
    path("price/history/<int:sneaker_id>/", get_price_history, name="get_price_history"),
]