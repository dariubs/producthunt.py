from flask import Flask
from flask import jsonify
from producthunt import ProductHunt

api_key = 'wtpXwVAiQ5gH2ahM1e9ziWe0bCuzOaqahVZfsZRaccI'
ph = ProductHunt(api_key)
app = Flask(__name__)


@app.route('/product-details')
def get_product_details():
    data = ph.get_product_details(slug='product')
    return jsonify(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)