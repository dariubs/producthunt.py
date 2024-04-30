from flask import Flask
from flask import jsonify
app = Flask(__name__)



@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)