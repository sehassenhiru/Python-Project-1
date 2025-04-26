from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Invalid email address!")
        return  # Exit the function if the email is invalid
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users available. Please create a user first.\n")
        return False
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")
    return True

def create_account():
    # Check if users exist before proceeding
    if not list_users():
        return
    
    # Safe user selection
    while True:
        try:
            idx = int(input("Select user number: ")) - 1
            if 0 <= idx < len(users):
                break
            else:
                print("Invalid user selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    
    # Safe account type selection
    while True:
        try:
            account_choice = int(input("Enter your choice (1, 2, 3): "))
            if 1 <= account_choice <= 3:
                break
            else:
                print("Invalid account type!")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")
    
    # Safe deposit amount input
    while True:
        try:
            amount = float(input("Enter initial deposit: "))
            if amount >= 0:
                break
            else:
                print("Initial deposit cannot be negative.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    # Check if users exist before proceeding
    if not list_users():
        return
    
    # Safe user selection
    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if 0 <= idx < len(users):
                user = users[idx]
                break
            else:
                print("Invalid user selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Check if user has accounts
    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return
    
    # Display user accounts
    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    # Safe account selection
    while True:
        try:
            acc_idx = int(input("Select account: ")) - 1
            if 0 <= acc_idx < len(user.accounts):
                break
            else:
                print("Invalid account selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Safe deposit amount input
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                user.accounts[acc_idx].deposit(amount)
                print("Deposit successful.\n")
                break
            else:
                print("Deposit amount must be positive.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

def withdraw_money():
    # Check if users exist before proceeding
    if not list_users():
        return
    
    # Safe user selection
    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if 0 <= idx < len(users):
                user = users[idx]
                break
            else:
                print("Invalid user selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Check if user has accounts
    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return
    
    # Display user accounts
    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    # Safe account selection
    while True:
        try:
            acc_idx = int(input("Select account: ")) - 1
            if 0 <= acc_idx < len(user.accounts):
                break
            else:
                print("Invalid account selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Safe withdrawal amount input
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                try:
                    user.accounts[acc_idx].withdraw(amount)
                    print("Withdrawal successful.\n")
                    break
                except ValueError as e:
                    print(f"Error: {e}\n")
                    break  # Exit withdrawal attempt after error
            else:
                print("Withdrawal amount must be positive.\n")
        except ValueError:
            print("Invalid input. Please enter a valid amount.\n")

def view_transactions():
    # Check if users exist before proceeding
    if not list_users():
        return
    
    # Safe user selection
    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if 0 <= idx < len(users):
                user = users[idx]
                break
            else:
                print("Invalid user selection.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    # Check if user has accounts
    if not user.accounts:
        print(f"{user.name} has no accounts yet.\n")
        return
    
    # Display transaction history for each account
    print(f"\n{user.name}'s Accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        if acc.get_transaction_history():
            print("Transaction History:")
            for tx in acc.get_transaction_history():
                print(tx)
        else:
            print("No transaction history yet.")

# Main menu
if __name__ == "__main__":
    while True:
        print("\nBanking System Menu:")
        print("1. Create User")
        print("2. List Users")
        print("3. Create Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            create_account()
        elif choice == '4':
            deposit_money()
        elif choice == '5':
            withdraw_money()
        elif choice == '6':
            view_transactions()
        elif choice == '7':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
