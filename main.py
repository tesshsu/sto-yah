from flask import Flask, jsonify, render_template
import yfinance as yf
import os
import threading
import time

app = Flask(__name__, 
            static_folder='src/static', 
            template_folder='src/static')

# List of top 20 stock symbols
top_stocks = [
    "AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NVDA", "BRK-B", 
    "JPM", "V", "WMT", "MA", "PG", "UNH", "HD", "DIS", "PYPL", "NFLX", 
    "ADBE", "CRM"
]

# Global variables for stock data
stock_data = {}
last_update_time = 0
update_lock = threading.Lock()

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="5d")
        if hist.empty:
            return None
        prices = hist['Close'].tolist()[-5:]
        if len(prices) < 2:
            return None
        current_price = prices[-1]
        previous_price = prices[0]
        percent_change = ((current_price - previous_price) / previous_price) * 100
        return {
            "current_price": round(current_price, 2),
            "price_history": [round(price, 2) for price in prices],
            "percent_change": round(percent_change, 2)
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def update_stock_data():
    """Updates stock data in the background"""
    global stock_data, last_update_time
    
    while True:
        print("Updating stock data...")
        temp_stock_data = {}
        
        for symbol in top_stocks:
            try:
                data = get_stock_data(symbol)
                if data:
                    stock_info = yf.Ticker(symbol).info
                    name = stock_info.get('longName', symbol)
                    temp_stock_data[name] = data
            except Exception as e:
                print(f"Error processing {symbol}: {e}")
        
        # Update the global stock data with lock to avoid race conditions
        with update_lock:
            stock_data = temp_stock_data
            last_update_time = time.time()
        
        # Sleep for 15 minutes before updating again
        time.sleep(900)  # 15 minutes in seconds

# Start the background thread to update stock data
update_thread = threading.Thread(target=update_stock_data, daemon=True)
update_thread.start()

@app.route('/')
def health_check():
    """Simple health check endpoint for GCP load balancer"""
    return jsonify({"status": "healthy"}), 200

@app.route('/stocks')
def home():
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    with update_lock:
        current_data = stock_data.copy()

    # If data hasn't been loaded yet, return empty but valid response
    if not current_data:
        return jsonify({"status": "loading", "data": {}}), 200

    return jsonify(current_data)

if __name__ == "__main__":
    # In production, this will be run by Gunicorn, not Flask's dev server
    app.run(host='0.0.0.0', port=8000)