from flask import Flask
from flask import jsonify
from producthunt import ProductHunt

api_key = ''
ph = ProductHunt(api_key)
app = Flask(__name__)


@app.route('/product-details')
def get_product_details():
    data = ph.get_product_details(slug='product')
    return jsonify(data)

@app.route('/get-daily')
def get_daily():
    data = ph.get_daily()
    return jsonify(data)

@app.route('/get-posts-by-topic')
def get_posts_by_topic():
    data = ph.get_posts_by_topic()
    return jsonify(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)