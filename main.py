from flask import Flask, jsonify, render_template
import yfinance as yf
import os

app = Flask(__name__, 
            static_folder='src/static', 
            template_folder='src/static')

# List of top 20 stock symbols
top_stocks = [
    "AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NVDA", "BRK-B", 
    "JPM", "V", "WMT", "MA", "PG", "UNH", "HD", "DIS", "PYPL", "NFLX", 
    "ADBE", "CRM"
]

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

stock_data = {}
for symbol in top_stocks:
    data = get_stock_data(symbol)
    if data:
        stock_info = yf.Ticker(symbol).info
        name = stock_info.get('longName', symbol)
        stock_data[name] = data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stocks')
def get_stocks():
    return jsonify(stock_data)

if __name__ == "__main__":
    # In production, this will be run by Gunicorn, not Flask's dev server
    app.run(host='0.0.0.0', port=8000)