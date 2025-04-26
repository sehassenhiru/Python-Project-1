class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self): 
        # Calculate the sum of all account balances
        total = sum(account.get_balance() for account in self.accounts)
        return total

    def get_account_count(self):
        # Return the actual count of accounts
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            return f"Account removed successfully"
        return "Account not found"

    def is_valid_email(self, email):
        # Basic email validation
        import re
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(email_pattern.match(email))

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance()}"