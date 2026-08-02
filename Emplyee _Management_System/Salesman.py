from EmployeeValidationException import *
from Employee import *
from Department import *
from Address import *

class Salesman(Employee):
    """Derived Class: Salesman."""

    def __init__(self, empname: str, salary: float, department: Department, address: Address, commission: float):
        super().__init__(empname, salary, department, address)
        self.set_commission(commission)

    def get_commission(self):
        return self._commission

    def set_commission(self, commission: float):
        if commission < 0:
            raise EmployeeValidationException("Commission cannot be negative.")
        self._commission = float(commission)

    def calculate_total_pay(self):
        return self.get_salary() + self._commission