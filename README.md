# producthunt.py

[![PyPI version](https://badge.fury.io/py/producthunt.svg)](https://badge.fury.io/py/producthunt)

Product Hunt API wrapper for python

## Installation

You can install with pip:

```
pip install producthunt
```

or from source code:

```shell
git clone repo
make local
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

### Get Posts by Topic

Fetch posts by topic:

```python
products = ph.get_posts_by_topic('artificial-intelligence')
for product in products:
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Tagline: {product['Tagline']}")
```



## Run it on Docker
- You can also clone the project and run it with docker exposing the function calls implemented as REST API endpoints. To do that follow these commands:

```
git clone https://github.com/dariubs/producthunt.py.git

```

- Add your API token that you get from ProductHunt
```
cd producthunt.py

open a file server.py then add it => api_key = 'product-hunt-token'

```

- Then build and run your docker container

```
cd producthunt.py

docker-compose up --build

```

- It will build and run the container on  `http://localhost:8000`. Endpoints are named based on the current implemented funtions:

```
/get-daily
/product-details
/get-posts-by-topic

```


## License

This project is licensed under the terms of the MIT license.


