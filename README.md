# producthunt.py

Fetch daily new products and details of specific products from Product Hunt.

## Installation

```
pip install producthunt
```

### init

First, initialize the ProductHunt class with your API key.

```python
from producthunt import ProductHunt
api_key = 'YOUR_API_KEY_HERE'
ph = ProductHunt(api_key)
```

### Get Daily Products

Fetch daily new products.

```python
daily_products = ph.get_daily()
for product in daily_products:
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Tagline: {product['Tagline']}")
```

### Get Product Details

Fetch the details of a specific product using its slug.

```python
product_details = ph.get_product_details("some-product-slug")
if product_details:
    print(f"Name: {product_details['Name']}")
    print(f"Tagline: {product_details['Tagline']}")
    print(f"Description: {product_details['Description']}")
    print(f"Website: {product_details['Website']}")
else:
    print("Product not found.")
```

### Get Products by Topic

Fetch products by topic:

```python
products = ph.get_products_by_topic('artificial-intelligence')
for product in products:
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Tagline: {product['Tagline']}")
```

## License

This project is licensed under the terms of the MIT license.


