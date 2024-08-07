import requests
from microservice import add_transaction, get_transactions

API_KEY = '0JctAjeE7hy18259S8P4XmvAAALTPG51'
BASE_URL = 'https://financialmodelingprep.com/api/v3'

def fetch_stock_price(symbol):
    # Fetch the current stock price for the given symbol
    url = f"{BASE_URL}/quote/{symbol}?apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['price']
    else:
        raise ValueError(f"Stock symbol {symbol} not found")

def perform_transaction(symbol, amount, transaction_type):
    # Perform a transaction and handle exceptions
    try:
        price = fetch_stock_price(symbol)
        response = add_transaction(price, amount, symbol, transaction_type)
        print(response)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # Example transactions
    perform_transaction("AAPL", 10, "buy")
    perform_transaction("GOOGL", 5, "sell")

    # Get and print transactions
    transactions = get_transactions()
    print(transactions)
