from Account import *
from Bank_User import *
from Customer import *

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
            raise BankValidationException(f"Transaction failed! Amount exceeds available balance and Overdraft limit of ${self.overdraft:.2f}.")
        
        self.balance -= amount
        print(f"[Success] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")