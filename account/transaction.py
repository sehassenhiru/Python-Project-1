from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type):
        # Validate amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Transaction amount must be a positive number")
            
        # Validate transaction type
        if transaction_type.lower() not in ["deposit", "withdraw"]:
            raise ValueError("Transaction type must be either 'deposit' or 'withdraw'")
            
        self.amount = amount
        self.transaction_type = transaction_type.lower()  # Normalize to lowercase
        self.timestamp = datetime.now()

    def __str__(self):
        # Format currency with INR symbol (Rs.) to match the rest of the application
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: Rs. {self.amount}"