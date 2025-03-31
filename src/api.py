from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

popular_stocks = [
    "AAPL", "GOOG", "GOOGL", "MSFT", "AMZN", "TSLA", "NVDA", "PYPL", "ADBE", "NFLX",
    "CMCSA", "PEP", "CSCO", "INTC", "QCOM", "TXN", "AVGO", "MU", "LRCX", "ADI"
]

@app.route("/")
def index():
    stock_prices = []
    for stock in popular_stocks:
        ticker = yf.Ticker(stock)
        info = ticker.info
        name = info["shortName"]
        price = info["currentPrice"]
        stock_prices.append((name, price))
    return render_template("index.html", stock_prices=stock_prices)

if __name__ == "__main__":
    app.run(debug=True)