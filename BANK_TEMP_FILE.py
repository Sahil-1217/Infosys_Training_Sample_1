"""Project 2: Banking Management System
Features:
- Parameterized Constructor
- Member Methods
- Centralized Validations & Custom Exceptions
- Base Class: Account (accid, balance, customer, deposit, withdraw)
- Derived Classes: SavingsAccount (minbalance), CurrentAccount (overdraft)
- Association: Customer (custid, custname, address, accounts), Address (street, city, pincode)
- Auto-generated Account and Customer IDs
- Driver Application: UseBankingApp
"""

import re


# ==========================================
# CUSTOM EXCEPTION
# ==========================================

class BankValidationException(Exception):
    """Custom exception class for banking validation errors."""
    pass


# ==========================================
# ASSOCIATED CLASSES
# ==========================================

class Address:
    """Address class (1-to-1 Association with Customer)."""

    def __init__(self, street: str, city: str, pincode: str):
        if not street or not street.strip():
            raise BankValidationException("Street cannot be empty.")
        self.street = street.strip()

        if not city or not city.strip():
            raise BankValidationException("City cannot be empty.")
        self.city = city.strip()

        # Validate 6-digit pincode
        pincode_str = str(pincode).strip()
        if not re.match(r"^\d{6}$", pincode_str):
            raise BankValidationException("Pincode must be exactly 6 digits.")
        self.pincode = pincode_str

    def display_address(self):
        return f"{self.street}, {self.city} - {self.pincode}"


class Customer:
    """
    Customer class.
    Relationship: 1 Customer to Many Accounts (using a set), 1 Customer to 1 Address.
    """
    _cust_counter = 5000

    def __init__(self, custname: str, address: Address):
        if not custname or not custname.strip():
            raise BankValidationException("Customer Name cannot be empty.")
        self.custname = custname.strip()

        if not isinstance(address, Address):
            raise BankValidationException("Invalid Address object.")
        self.address = address

        # Auto-generate Customer ID
        Customer._cust_counter += 1
        self.custid = Customer._cust_counter

        # 1-to-Many: Set to store multiple accounts uniquely
        self.accounts = set()

    # Magic methods to allow storing Customer objects in Python sets/dicts
    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.custid == other.custid
        return False

    def __hash__(self):
        return hash(self.custid)

    # Methods to manage 1-to-Many Set Association
    def add_account(self, account):
        """Adds an account to the customer's set."""
        self.accounts.add(account)

    def remove_account(self, account):
        """Removes an account from the customer's set."""
        self.accounts.discard(account)

    def get_accounts(self):
        """Returns the set of accounts owned by this customer."""
        return self.accounts

    def display_customer_details(self):
        print(f"Customer ID: {self.custid} | Name: {self.custname}")
        print(f"Address: {self.address.display_address()}")

    def display_all_customer_accounts(self):
        """Displays details of all accounts held in this customer's set."""
        print(f"\n--- Accounts for Customer: {self.custname} (ID: {self.custid}) ---")
        if not self.accounts:
            print("No accounts associated with this customer.")
        else:
            for acc in self.accounts:
                print(f" -> Account ID: {acc.accid} | Type: {acc.__class__.__name__} | Balance: ${acc.balance:.2f}")


# ==========================================
# BASE ACCOUNT CLASS
# ==========================================

class Account:
    """
    Base Class with Auto-generated ID.
    Relationship: 1 Account to 1 Customer.
    """
    _acc_counter = 10000

    def __init__(self, balance: float, customer: Customer):
        if balance < 0:
            raise BankValidationException("Initial balance cannot be negative.")
        self.balance = float(balance)

        if not isinstance(customer, Customer):
            raise BankValidationException("Invalid Customer object.")

        # Auto-generate Account ID
        Account._acc_counter += 1
        self.accid = Account._acc_counter

        # 1-to-1 link from Account back to Customer
        self.customer = customer

        # Bi-directional sync: Add this account to the customer's set
        self.customer.add_account(self)

    # Magic methods to allow storing Account objects uniquely inside a Python Set
    def __eq__(self, other):
        if isinstance(other, Account):
            return self.accid == other.accid
        return False

    def __hash__(self):
        return hash(self.accid)

    def deposit(self, amount: float):
        if amount <= 0:
            raise BankValidationException("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"[Success] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise BankValidationException("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise BankValidationException("Insufficient funds!")
        self.balance -= amount
        print(f"[Success] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_account_details(self):
        print(f"Account ID: {self.accid} | Account Type: {self.__class__.__name__}")
        print(f"Balance: ${self.balance:.2f}")
        self.customer.display_customer_details()


# ==========================================
# DERIVED CLASSES
# ==========================================

class SavingsAccount(Account):
    """Derived Class: SavingsAccount."""

    def __init__(self, balance: float, customer: Customer, minbalance: float = 1000.0):
        if minbalance < 0:
            raise BankValidationException("Minimum balance limit cannot be negative.")
        self.minbalance = float(minbalance)

        # Ensure initial balance meets minimum requirement
        if balance < self.minbalance:
            raise BankValidationException(f"Savings account needs a minimum initial deposit of ${self.minbalance:.2f}.")

        super().__init__(balance, customer)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise BankValidationException("Withdrawal amount must be greater than zero.")
        # Check if withdrawal causes balance to drop below minimum requirement
        if (self.balance - amount) < self.minbalance:
            raise BankValidationException(
                f"Transaction failed! Minimum balance of ${self.minbalance:.2f} must be maintained."
            )
        self.balance -= amount
        print(f"[Success] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")


class CurrentAccount(Account):
    """Derived Class: CurrentAccount."""

    def __init__(self, balance: float, customer: Customer, overdraft: float = 5000.0):
        if overdraft < 0:
            raise BankValidationException("Overdraft limit cannot be negative.")
        self.overdraft = float(overdraft)

        super().__init__(balance, customer)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise BankValidationException("Withdrawal amount must be greater than zero.")
        # Allow withdrawal up to balance + overdraft allowance
        if amount > (self.balance + self.overdraft):
            raise BankValidationException(
                f"Transaction failed! Amount exceeds available balance and Overdraft limit of ${self.overdraft:.2f}."
            )
        self.balance -= amount
        print(f"[Success] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")


# ==========================================
# DRIVER METHOD (UseBankingApp)
# ==========================================

def get_or_create_customer(customers_dict: dict) -> Customer:
    """Helper to reuse an existing customer profile or create a new one."""
    if customers_dict:
        print("\nExisting Customers:")
        for custid, cust in customers_dict.items():
            print(f" - ID {custid}: {cust.custname}")

        use_existing = input("Link account to an existing customer? (y/n): ").strip().lower()
        if use_existing == 'y':
            target_id = int(input("Enter Customer ID: "))
            if target_id in customers_dict:
                return customers_dict[target_id]
            else:
                print("Customer ID not found. Proceeding to create a new customer...")

    print("\n-- Enter New Customer Details --")
    custname = input("Enter Customer Name: ")

    print("\n-- Enter Address Details --")
    street = input("Street: ")
    city = input("City: ")
    pincode = input("Pincode (6 digits): ")
    address = Address(street, city, pincode)

    customer = Customer(custname, address)
    customers_dict[customer.custid] = customer
    return customer


def UseBankingApp():
    accounts_list = []
    customers_dict = {} # Map of custid -> Customer object

    while True:
        print("\n" + "=" * 40)
        print(" BANKING MANAGEMENT SYSTEM ")
        print("=" * 40)
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Display All Accounts")
        print("6. View Accounts by Customer (Set View)")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice in ["1", "2"]:
            try:
                customer = get_or_create_customer(customers_dict)

                print("\n-- Enter Account Details --")
                balance = float(input("Enter Initial Balance: "))

                if choice == "1":
                    minbalance = float(input("Enter Minimum Balance required (e.g. 1000): "))
                    acc = SavingsAccount(balance, customer, minbalance)
                elif choice == "2":
                    overdraft = float(input("Enter Overdraft Limit (e.g. 5000): "))
                    acc = CurrentAccount(balance, customer, overdraft)

                accounts_list.append(acc)
                print(f"\n[Success] {acc.__class__.__name__} Created with Auto Account ID: {acc.accid}")

            except BankValidationException as bve:
                print(f"\n[Validation Error]: {bve}")
            except ValueError:
                print("\n[Input Error]: Please enter numeric values where required.")
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice in ["3", "4"]:
            if not accounts_list:
                print("\nNo accounts available. Create an account first!")
                continue
            try:
                acc_id = int(input("Enter Account ID: "))
                target_acc = None
                for acc in accounts_list:
                    if acc.accid == acc_id:
                        target_acc = acc
                        break

                if target_acc is None:
                    print("\n[Error]: Account ID not found.")
                else:
                    amt = float(input("Enter Amount: "))
                    if choice == "3":
                        target_acc.deposit(amt)
                    elif choice == "4":
                        target_acc.withdraw(amt)
            except BankValidationException as bve:
                print(f"\n[Validation Error]: {bve}")
            except ValueError:
                print("\n[Input Error]: Please enter a valid number.")

        elif choice == "5":
            if not accounts_list:
                print("\nNo account records found.")
            else:
                print("\n" + "-" * 40)
                for acc in accounts_list:
                    acc.display_account_details()
                    print("-" * 40)

        elif choice == "6":
            if not customers_dict:
                print("\nNo customers registered yet.")
            else:
                cust_id = int(input("Enter Customer ID to view their accounts: "))
                if cust_id in customers_dict:
                    customers_dict[cust_id].display_all_customer_accounts()
                else:
                    print("Customer ID not found.")

        elif choice == "7":
            print("\nExiting Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 7.")


if __name__ == "__main__":
    UseBankingApp()
