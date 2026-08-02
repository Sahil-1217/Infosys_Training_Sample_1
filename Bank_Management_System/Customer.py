from Bank_User import *
from Account import *
from Address import *

class Customer:
    """Customer class (Association with Account and Address)."""
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
        
        # Customer can hold multiple accounts
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_customer_details(self):
        print(f"Customer ID: {self.custid} | Name: {self.custname}")
        print(f"Address: {self.address.display_address()}")