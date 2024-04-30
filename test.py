
from producthunt import ProductHunt
api_key = 'wtpXwVAiQ5gH2ahM1e9ziWe0bCuzOaqahVZfsZRaccI'
ph = ProductHunt(api_key)


daily_products = ph.get_daily()
for product in daily_products:
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Tagline: {product['Tagline']}")


