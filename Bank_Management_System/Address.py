from Bank_User import *
from Account import *
from BankValidationException import *


class Address:
    """Address class (Association with Customer)."""

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