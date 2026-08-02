from EmployeeValidationException import *
from Employee import *

class Address:
    """Address class (Association with Employee)."""

    def __init__(self, street: str, city: str, pincode: str):
        self.set_street(street)
        self.set_city(city)
        self.set_pincode(pincode)

    # Getters and Setters
    def get_street(self):
        return self._street

    def set_street(self, street: str):
        if not street or not street.strip():
            raise EmployeeValidationException("Street cannot be empty.")
        self._street = street.strip()

    def get_city(self):
        return self._city

    def set_city(self, city: str):
        if not city or not city.strip():
            raise EmployeeValidationException("City cannot be empty.")
        self._city = city.strip()

    def get_pincode(self):
        return self._pincode

    def set_pincode(self, pincode: str):
        pincode_str = str(pincode).strip()
        if not re.match(r"^\d{6}$", pincode_str):
            raise EmployeeValidationException("Pincode must be exactly 6 digits.")
        self._pincode = pincode_str

    def display_address(self):
        return f"{self._street}, {self._city} - {self._pincode}"