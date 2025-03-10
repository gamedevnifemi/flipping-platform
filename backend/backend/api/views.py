from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.db.models import Sneaker, SneakerPriceHistory
from django.utils.timezone import now
from .serializers import SneakerSerializer
from django.core.paginator import Paginator
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

    page = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)

    """Get all sneakers from the database"""
    sneakers = Sneaker.objects.all()
    paginator = Paginator(sneakers, per_page)
    paginated_sneakers = paginator.get_page(page)

    serializer = SneakerSerializer(paginated_sneakers, many=True)
    return Response({
        "products": serializer.data,
        "total_pages": paginator.num_pages,
        "current_page": paginated_sneakers.number
    })

@api_view(["GET"])
def get_price_history(request, sneaker_id):
    """Retrieve price history for a sneaker"""
    try:
        sneaker = Sneaker.objects.get(id=sneaker_id)
        price_history = SneakerPriceHistory.objects.filter(sneaker=sneaker).order_by("recorded_at")

        data = [
            {
                "date": entry.recorded_at.strftime("%Y-%m-%d"),
                "stockX_price": entry.stockx_price,
                "goat_price": entry.goat_price
            }
            for entry in price_history
        ]

        return Response({"sneaker": sneaker.shoe_name, "price_history": data})

    except Sneaker.DoesNotExist:
        return Response({"error": "Sneaker not found."}, status=404)
