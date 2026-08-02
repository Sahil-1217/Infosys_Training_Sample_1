from EmployeeValidationException import *
from Employee import *
from Department import *
from Address import *

class Employee:
    """Base Class with Auto-generated ID."""
    _id_counter = 1000

    def __init__(self, empname: str, salary: float, department: Department, address: Address):
        # Auto-generate ID
        Employee._id_counter += 1
        self._empid = Employee._id_counter

        self.set_empname(empname)
        self.set_salary(salary)
        self.set_department(department)
        self.set_address(address)

    # Getters and Setters
    def get_empid(self):
        return self._empid

    def get_empname(self):
        return self._empname

    def set_empname(self, empname: str):
        if not empname or not empname.strip():
            raise EmployeeValidationException("Employee Name cannot be empty.")
        self._empname = empname.strip()

    def get_salary(self):
        return self._salary

    def set_salary(self, salary: float):
        if salary < 0:
            raise EmployeeValidationException("Salary cannot be negative.")
        self._salary = float(salary)

    def get_department(self):
        return self._department

    def set_department(self, department: Department):
        if not isinstance(department, Department):
            raise EmployeeValidationException("Invalid Department object.")
        self._department = department

    def get_address(self):
        return self._address

    def set_address(self, address: Address):
        if not isinstance(address, Address):
            raise EmployeeValidationException("Invalid Address object.")
        self._address = address

    def calculate_total_pay(self):
        return self._salary

    def display_details(self):
        print(f"ID: {self._empid} | Name: {self._empname} | Role: {self.__class__.__name__}")
        print(f"Base Salary: ${self._salary:.2f} | Total Pay: ${self.calculate_total_pay():.2f}")
        print(f"Department: {self._department.display_dept()}")
        print(f"Address: {self._address.display_address()}")
