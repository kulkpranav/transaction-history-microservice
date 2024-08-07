import json
import os

TRANSACTIONS_FILE = 'transactions.json'

def load_transactions():
    # Load transactions from the file, return an empty list if file doesn't exist
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    with open(TRANSACTIONS_FILE, 'r') as file:
        return json.load(file)

def save_transactions(transactions):
    # Save transactions to the file
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(price, amount, symbol, transaction_type):
    # Add a new transaction and save it
    transactions = load_transactions()
    transaction = {
        "price": price,
        "amount": amount,
        "symbol": symbol,
        "type": transaction_type  # 'buy' or 'sell'
    }
    transactions.append(transaction)
    save_transactions(transactions)
    return {"message": "Transaction added successfully"}

def get_transactions():
    # Retrieve all transactions
    return load_transactions()

if __name__ == '__main__':
    pass  # Microservice entry point
