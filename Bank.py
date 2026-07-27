from abc import ABC, abstractmethod
import random

# --- Parent Abstract Class ---
class Account(ABC):
    def __init__(self, account_no, holder_name, balance=0.0):
        # 1. Validate Account Number
        if account_no <= 0:
            raise ValueError(f"Invalid Account No ({account_no}). Must be greater than 0!")
        
        # 2. Validate Name
        if not holder_name or not holder_name.strip():
            raise ValueError("Account holder name cannot be blank!")
            
        # 3. Validate Opening Balance
        if balance < 0:
            raise ValueError(f"Initial balance (₹{balance}) cannot be negative!")

        self.account_no = account_no
        self.holder_name = holder_name.strip()
        self.balance = float(balance)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_details(self):
        return f"Acc No: {self.account_no} | Holder: {self.holder_name} | Balance: ₹{self.balance:.2f}"


# --- Child Class 1: Savings Account ---
class SavingsAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, min_balance=1000.0):
        super().__init__(account_no, holder_name, balance)
        
        if min_balance < 0:
            raise ValueError("Minimum balance limit cannot be negative!")
        self.min_balance = float(min_balance)

    def deposit(self, amount):
        if amount <= 0:
            return "Error: Deposit amount must be greater than 0!"
        self.balance += amount
        return f"Successfully deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"

    def withdraw(self, amount):
        # Conditional Validation for Savings Account
        if amount <= 0:
            return "Error: Withdrawal amount must be greater than 0!"
        if self.balance - amount < self.min_balance:
            return f"Transaction Denied! Savings account must maintain a minimum balance of ₹{self.min_balance:.2f}."
        
        self.balance -= amount
        return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"

    def show_details(self):
        base_details = super().show_details()
        return f"[Savings] {base_details} | Min Balance Req: ₹{self.min_balance:.2f}"


# --- Child Class 2: Current Account ---
class CurrentAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_no, holder_name, balance)
        
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative!")
        self.overdraft_limit = float(overdraft_limit)

    def deposit(self, amount):
        if amount <= 0:
            return "Error: Deposit amount must be greater than 0!"
        self.balance += amount
        return f"Successfully deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"

    def withdraw(self, amount):
        # Conditional Validation for Current Account (Allows overdraft)
        if amount <= 0:
            return "Error: Withdrawal amount must be greater than 0!"
        if self.balance - amount < -self.overdraft_limit:
            return f"Transaction Denied! Exceeds your overdraft limit of ₹{self.overdraft_limit:.2f}."
        
        self.balance -= amount
        return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"

    def show_details(self):
        base_details = super().show_details()
        return f"[Current] {base_details} | Overdraft Limit: ₹{self.overdraft_limit:.2f}"


# --- Main Execution & User Menu ---
def run_banking_system():
    print("=== Welcome to the Banking Management System ===")
    
    # User Input for Account Creation
    try:
        name = input("Enter Account Holder Name: ")
        acc_type = input("Enter Account Type (Savings / Current): ").strip().lower()
        initial_deposit = float(input("Enter Initial Deposit Amount: "))
        
        # Generate a random account number like your reference code
        acc_no = random.randint(10000, 99999)
        
        # Instantiate object based on type
        if acc_type == "savings":
            account = SavingsAccount(acc_no, name, initial_deposit)
        elif acc_type == "current":
            account = CurrentAccount(acc_no, name, initial_deposit)
        else:
            print("Invalid account type selected. Defaulting to Savings Account.")
            account = SavingsAccount(acc_no, name, initial_deposit)
            
        print("\n[SUCCESS] Account Created Successfully!")
        print(account.show_details())
        
        # Interactive Transaction Loop
        while True:
            print("\n--- Banking Menu ---")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Show Account Details")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":
                amt = float(input("Enter amount to deposit: "))
                message = account.deposit(amt)
                print(message)
                
            elif choice == "2":
                amt = float(input("Enter amount to withdraw: "))
                message = account.withdraw(amt)
                print(message)
                
            elif choice == "3":
                print("\n--- Current Details ---")
                print(account.show_details())
                
            elif choice == "4":
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice! Please select between 1 and 4.")
                
    except ValueError as error:
        print(f"\n[VALIDATION ERROR CATCHED]: {error}")
    except Exception as e:
        print(f"\n[ERROR]: An unexpected error occurred: {e}")

# Start the application
if __name__ == "__main__":
    run_banking_system()
