import requests
import environ

env = environ.Env()
# Get the Sneak-Api url
STOCKX_SERVICE_URL = env('STOCKX_SERVICE_URL')

def get_stockx_products():
    try:
        response = requests.get(STOCKX_SERVICE_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching StockX data: {e}")
        return None
