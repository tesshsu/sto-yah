from flask import Flask, jsonify, render_template
import os

app = Flask(__name__, 
            static_folder='src/static', 
            template_folder='src/static')

# Example stock data (replace with your actual logic to fetch stock prices)
stock_data = {
    "Apple Inc.": 219.45,
    "Alphabet Inc.": 153.55,
    "Microsoft Corporation": 368.15,
    # Add the rest of your stock data here
}

@app.route('/')
def home():
    # Serve the index.html template
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    # Return stock prices as JSON
    return jsonify(stock_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)