from abc import ABC, abstractmethod
import random

# --- Custom Banking Exceptions ---
class BankingException(Exception):
    """Base exception for all errors inside the Banking System."""
    pass

class InsufficientFundsError(BankingException):
    """Raised when an account cannot fulfill a withdrawal constraint."""
    pass

class InvalidTransactionError(BankingException):
    """Raised when deposit or withdrawal rules are violated."""
    pass

class ValidationError(BankingException):
    """Raised when initializing or setting data values incorrectly."""
    pass


# --- Base Abstract Class ---
class Account(ABC):
    def __init__(self, account_no, holder_name, balance=0.0):
        # Every step in initialization is safely guarded by methods throwing custom exceptions
        self.set_account_no(account_no)
        self.set_holder_name(holder_name)
        self.set_balance(balance)
        
    def set_holder_name(self, holder_name):
        # Strict checking for empty, null, or blank strings
        if not holder_name or not str(holder_name).strip():
            raise ValidationError("Account holder name cannot be empty or blank!")
        self.holder_name = str(holder_name).strip()   
         
    def set_account_no(self, account_no):
        # Prevent numbers below or equal to zero, and non-integers
        if not isinstance(account_no, int) or account_no <= 0:
            raise ValidationError(f"Invalid Account No ({account_no}). Must be an integer greater than 0!")
        self.account_no = account_no
        
    def set_balance(self, balance):
        # Secure the data layer against negative injections
        if balance < 0:
            raise ValidationError(f"Initial balance (₹{balance}) cannot be negative!")
        self.balance = float(balance)        

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_details(self):
        # Inner try-catch protects string formatting failures if attributes ever get corrupted
        try:
            return f"Acc No: {self.account_no} | Holder: {self.holder_name} | Balance: ₹{self.balance:.2f}"
        except Exception as e:
            raise BankingException(f"Failed to compile account details display: {e}")


# --- Savings Account Class ---
class SavingsAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, min_balance=1000.0):
        # Inherit base guardrails
        super().__init__(account_no, holder_name, balance)
        self.set_min_balance(min_balance)
                
    def set_min_balance(self, min_balance):
        if min_balance < 0:
            raise ValidationError("Minimum balance threshold constraint cannot be negative!")
        self.min_balance = float(min_balance)    

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Deposit value (₹{amount}) must be greater than zero!")
            self.balance += amount
            return f"Successfully deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Deposit operation rejected! Amount input must be a numeric value.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Withdrawal value (₹{amount}) must be greater than zero!")
            if self.balance - amount < self.min_balance:
                raise InsufficientFundsError(
                    f"Transaction Denied! Savings balance must stay above ₹{self.min_balance:.2f}."
                )
            self.balance -= amount
            return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Withdrawal operation rejected! Amount input must be a numeric value.")

    def show_details(self):
        # Nested execution catches base class format errors and layers custom details on top safely
        try:
            base_details = super().show_details()
            return f"[Savings] {base_details} | Min Balance Req: ₹{self.min_balance:.2f}"
        except BankingException as e:
            raise BankingException(f"Savings Account details generation failed: {e}")


# --- Current Account Class ---
class CurrentAccount(Account):
    def __init__(self, account_no, holder_name, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_no, holder_name, balance)
        self.set_overdraft_limit(overdraft_limit)
        
    def set_overdraft_limit(self, overdraft_limit):
        if overdraft_limit < 0:
            raise ValidationError("Overdraft protection ceiling limit cannot be negative!")
        self.overdraft_limit = float(overdraft_limit)
        
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Deposit value (₹{amount}) must be greater than zero!")
            self.balance += amount
            return f"Successfully deposited ₹{amount:.2f}. New Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Deposit operation rejected! Amount input must be a numeric value.")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise InvalidTransactionError(f"Withdrawal value (₹{amount}) must be greater than zero!")
            if self.balance - amount < -self.overdraft_limit:
                raise InsufficientFundsError(
                    f"Transaction Denied! Balance cannot fall lower than overdraft limit (-₹{self.overdraft_limit:.2f})."
                )
            self.balance -= amount
            return f"Successfully withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}"
        except TypeError:
            raise InvalidTransactionError("Withdrawal operation rejected! Amount input must be a numeric value.")

    def show_details(self):
        try:
            base_details = super().show_details()
            return f"[Current] {base_details} | Overdraft Limit: ₹{self.overdraft_limit:.2f}"
        except BankingException as e:
            raise BankingException(f"Current Account details generation failed: {e}")


# --- Runtime Flow UI and Interface Engine ---
