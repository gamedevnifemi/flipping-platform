from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.db.models import Sneaker
from django.utils.timezone import now
from .serializers import SneakerSerializer
from .services.stockx_service import get_stockx_products

@api_view(["GET"])
def fetch_products(request):
    products = get_stockx_products()
    
    if not products:
        return Response({
            "error": "Failed to fetch products from StockX service. Make sure the service is running on port 5001."
        }, status=500)

    successful_count = 0
    errors = []

    for product in products:
        try:
            sneaker, created = Sneaker.objects.update_or_create(
                style_id=product.get("styleID"),
                defaults={
                    "shoe_name": product.get("shoeName", "Unknown"),
                    "retail_price": product.get("retailPrice", 0.0),
                    "thumbnail": product.get("thumbnail", ""),
                    "description": product.get("description", ""),
                    "brand": product.get("brand", ""),
                    "colorway": product.get("colorway", ""),
                    "stockx_url": product.get("resellLinks", {}).get("stockx", ""),
                    "goat_url": product.get("resellLinks", {}).get("goat", ""),
                    "last_updated": now()
                }
            )
            successful_count += 1
        except Exception as e:
            errors.append(f"Error processing product {product.get('styleID')}: {str(e)}")
            continue

    return Response({
        "message": "Sneakers update completed",
        "successful": successful_count,
        "errors": errors if errors else None
    })

@api_view(["GET"])
def get_sneakers(request):
    """Get all sneakers from the database"""
    sneakers = Sneaker.objects.all()
    serializer = SneakerSerializer(sneakers, many=True)
    return Response(serializer.data)