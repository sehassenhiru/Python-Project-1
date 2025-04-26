from account.transaction import Transaction
from account.user import User

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Invalid initial balance!")
            # Set to default value when invalid
            initial_balance = 0
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.user = User(name, email)

    def deposit(self, amount):
        # Fix Issue #2: Ensure balance consistency by proper validation
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount is invalid!")
            return False
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))
        return True

    def withdraw(self, amount):
        # Fix Issue #2: Ensure balance consistency with proper validation and error handling
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
        if self.balance < amount:
            raise ValueError("Insufficient Balance!")
        self.balance -= amount  # Critical fix for Issue #2: Subtraction for withdrawal
        self.transactions_history.append(Transaction(amount, "withdraw"))
        return True

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user

class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        # Fix Issue #2: Ensure proper validation before withdrawal
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
            
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"A minimum balance of Rs.{self.MIN_BALANCE} needed for a Savings account!")
            
        return super().withdraw(amount)  # Return the result from the parent method

    def get_account_type(self):
        return "Savings account"

class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current account"

class StudentAccount(BankAccount):
    MIN_BALANCE = 100
    
    def withdraw(self, amount):
        # Fix Issue #2: Ensure proper validation before withdrawal
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return False
            
        if (self.balance - amount) < self.MIN_BALANCE:
            raise ValueError(f"A minimum balance of Rs.{self.MIN_BALANCE} needed to withdraw from a Students account!")
            
        return super().withdraw(amount)  # Return the result from the parent method

    def get_account_type(self):
        return "Students account"
