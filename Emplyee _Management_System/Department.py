from EmployeeValidationException import *
from Employee import *
from Department import *
from Address import *

class Department:
    """Department class (Association with Employee)."""

    def __init__(self, deptid: int, deptname: str, location: str):
        self.set_deptid(deptid)
        self.set_deptname(deptname)
        self.set_location(location)

    # Getters and Setters
    def get_deptid(self):
        return self._deptid

    def set_deptid(self, deptid: int):
        if deptid <= 0:
            raise EmployeeValidationException("Department ID must be greater than 0.")
        self._deptid = deptid

    def get_deptname(self):
        return self._deptname

    def set_deptname(self, deptname: str):
        if not deptname or not deptname.strip():
            raise EmployeeValidationException("Department Name cannot be empty.")
        self._deptname = deptname.strip()

    def get_location(self):
        return self._location

    def set_location(self, location: str):
        if not location or not location.strip():
            raise EmployeeValidationException("Location cannot be empty.")
        self._location = location.strip()

    def display_dept(self):
        return f"{self._deptname} (ID: {self._deptid}, Location: {self._location})"

