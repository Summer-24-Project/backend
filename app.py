from flask import Flask, request, jsonify, abort
from pricing import black_scholes

app = Flask(__name__)

# Hard-coded API key
API_KEY = 'your_secret_key_here'

@app.route('/')
def home():
    return "Welcome to the API! Use the /price endpoint to get started."

def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if api_key != API_KEY:
            abort(401, description="Unauthorized")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/price', methods=['POST'])
@require_api_key
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
