from flask import Flask, request, jsonify
from pricing import black_scholes

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def price():
    data = request.get_json()
    S = data['S']
    K = data['K']
    T = data['T']
    r = data['r']
    sigma = data['sigma']
    option_type = data['option_type']

    price = black_scholes(S, K, T, r, sigma, option_type)
    
    return jsonify({"price": price})

if __name__ == '__main__':
    app.run(debug=True)
