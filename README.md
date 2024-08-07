# Stock Transaction History Microservice
This repository contains a stock transaction microservice and a test program that demonstrates its functionality. The microservice allows you to record transactions (buy/sell) and retrieve the transaction history.
## Microservice Components
- 'microservice.py': The main microservice file that processes transaction requests and manages transaction history.
- 'test_program.py': A test program acting as a client to send requests to the microservice and receive responses.
- 'transactions.json': A JSON file used to store transaction history.
## How to Programmatically REQUEST Data from the Microservice
The data request to the microservice is done by calling functions directly. The add_transaction function is used to record a new transaction.
### Example Call to REQUEST Data
To add a transaction, call the 'add_transaction function' with the required parameters.
```python
from microservice import add_transaction

response = add_transaction(150, 5, "AAPL", "buy")
print(response)
```
## How to Programmatically REQUEST Data from the Microservice
The response from the microservice can be obtained by calling the get_transactions function, which retrieves the entire transaction history.
### Example Call to RECEIVE Data
To get the transaction history, call the 'get_transactions' function.
```python
from microservice import get_transactions

transactions = get_transactions()
print(transactions)
```
## UML Sequence Diagram:
