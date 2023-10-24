# producthunt.py
import json
import requests
from graphene import ObjectType, String, Schema

class Product(ObjectType):
    name = String()
    tagline = String()

class Query(ObjectType):
    product = String()

def fetch_data(query, api_key):
    url = 'https://api.producthunt.com/v2/api/graphql'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, json={'query': query})
    return response.json()

class ProductHunt:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_daily(self):
        query = '''
        query {
          posts(order: NEWEST, first: 10) {
            edges {
              node {
                id
                name
                tagline
              }
            }
          }
        }
        '''
        data = fetch_data(query, self.api_key)
        products = data.get('data', {}).get('posts', {}).get('edges', [])
        
        product_list = []
        for edge in products:
            product = edge.get('node', {})
            product_list.append({
                'ID': product.get('id'),
                'Name': product.get('name'),
                'Tagline': product.get('tagline'),
            })
        
        return product_list
