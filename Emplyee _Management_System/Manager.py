from EmployeeValidationException import *
from Employee import *
from Department import *
from Address import *

class Manager(Employee):
    """Derived Class: Manager."""

    def __init__(self, empname: str, salary: float, department: Department, address: Address, perks: float):
        super().__init__(empname, salary, department, address)
        self.set_perks(perks)

    def get_perks(self):
        return self._perks

    def set_perks(self, perks: float):
        if perks < 0:
            raise EmployeeValidationException("Perks cannot be negative.")
        self._perks = float(perks)

    def calculate_total_pay(self):
        return self.get_salary() + self._perks
