from EmployeeValidationException import *
from Employee import *
from Department import *
from Address import *

class Clerk(Employee):
    """Derived Class: Clerk."""

    def __init__(self, empname: str, salary: float, department: Department, address: Address, overtime: float):
        super().__init__(empname, salary, department, address)
        self.set_overtime(overtime)

    def get_overtime(self):
        return self._overtime

    def set_overtime(self, overtime: float):
        if overtime < 0:
            raise EmployeeValidationException("Overtime pay cannot be negative.")
        self._overtime = float(overtime)

    def calculate_total_pay(self):
        return self.get_salary() + self._overtime