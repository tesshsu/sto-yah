from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, 
            static_folder='src/static', 
            template_folder='src/static')

# Example stock data with price history and percentage change
stock_data = {
    "Apple Inc.": {
        "current_price": 219.45,
        "price_history": [218.50, 219.00, 218.80, 219.20, 219.45],
        "percent_change": 0.43
    },
    "Alphabet Inc.": {
        "current_price": 153.55,
        "price_history": [152.80, 153.00, 153.20, 153.40, 153.55],
        "percent_change": 0.49
    },
    "Microsoft Corporation": {
        "current_price": 368.15,
        "price_history": [367.00, 367.50, 367.80, 368.00, 368.15],
        "percent_change": 0.31
    },
    "Tesla, Inc": {
       "current_price": 248.62,
       "price_history": [247.50, 248.00, 248.20, 248.40, 248.62],
       "percent_change": 0.46
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)