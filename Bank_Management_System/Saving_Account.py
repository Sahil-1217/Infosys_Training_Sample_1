from Bank_User import *
from Account import *
from Customer import *

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
            raise BankValidationException(f"Transaction failed! Minimum balance of ${self.minbalance:.2f} must be maintained.")
        
        self.balance -= amount
        print(f"[Success] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")