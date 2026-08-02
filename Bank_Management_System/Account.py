from Bank_User import *
import re 
from BankValidationException import *
from Customer import *


class Account:
    """Base Class with Auto-generated ID."""
    _acc_counter = 10000

    def __init__(self, balance: float, customer: Customer):
        if balance < 0:
            raise BankValidationException("Initial balance cannot be negative.")
        self.balance = float(balance)

        if not isinstance(customer, Customer):
            raise BankValidationException("Invalid Customer object.")
        self.customer = customer

        # Auto-generate Account ID
        Account._acc_counter += 1
        self.accid = Account._acc_counter

        # Link this account to customer
        self.customer.add_account(self)

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
