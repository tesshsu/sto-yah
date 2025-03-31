# Stock App

This project is a simple Python application that retrieves the top 20 U.S. stocks using an open source API. It demonstrates how to fetch, process, and display stock data for companies like TSLA, GOOGL, NVDA, and more.

## Requirements

* Python 3.8+
* yfinance
* tkinter

## Features

- **Fetch Stock Data:** Retrieves the top 20 U.S. stocks from a configurable API endpoint.
- **Modular Design:** Uses a clean code structure that separates API calls and utility functions.
- **Easy to Extend:** Provides a foundation that can be expanded with additional functionality such as filtering or caching.

## structure
stock-app/
├── README.md
├── requirements.txt
├── main.py              # Backend application
├── Dockerfile           # Docker setup
├── docker-compose.yml   # Docker Compose setup
└── src/
    ├── __init__.py
    ├── api.py           # Backend API logic
    └── static/
        ├── index.html   # Frontend HTML file
        ├── app.js       # Frontend JavaScript file
        └── styles.css   # Frontend CSS file


## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/stock-app.git

## Run project
- docker-compose up --build

## Access the app
- Backend API at http://localhost:5000/api/stocks
- Frontend at http://localhost:5000