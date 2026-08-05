import re


# ==========================================
# CUSTOM EXCEPTION
# ==========================================
#here is the new code .

class EmployeeValidationException(Exception):
    """Custom exception class for validation errors."""
    pass


# ==========================================
# ASSOCIATED CLASSES
# ==========================================

class Address:
    """Address class (1-to-1 Association with Employee)."""

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


class Department:
    """
    Department class.
    Relationship: 1 Department to Many Employees (using a set).
    """

    def __init__(self, deptid: int, deptname: str, location: str):
        self.set_deptid(deptid)
        self.set_deptname(deptname)
        self.set_location(location)
        # 1-to-Many: Set to keep track of uniquely assigned employees
        self._employees = set()

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

    # Methods to manage 1-to-Many Set Association
    def add_employee(self, employee):
        """Adds an employee to the department's set."""
        self._employees.add(employee)

    def remove_employee(self, employee):
        """Removes an employee from the department's set."""
        self._employees.discard(employee)

    def get_employees(self):
        """Returns the set of employees in this department."""
        return self._employees

    def display_dept(self):
        return f"{self._deptname} (ID: {self._deptid}, Location: {self._location})"

    def display_all_department_employees(self):
        """Prints details of all employees in this department."""
        print(f"\n--- Employees in Department: {self._deptname} (ID: {self._deptid}) ---")
        if not self._employees:
            print("No employees assigned to this department yet.")
        else:
            for emp in self._employees:
                print(f" -> ID: {emp.get_empid()} | Name: {emp.get_empname()} | Role: {emp.__class__.__name__}")


# ==========================================
# BASE EMPLOYEE CLASS
# ==========================================

class Employee:
    """
    Base Class with Auto-generated ID.
    Relationship: 1 Employee to 1 Department, 1 Employee to 1 Address.
    """
    _id_counter = 1000

    def __init__(self, empname: str, salary: float, department: Department, address: Address):
        # Auto-generate ID
        Employee._id_counter += 1
        self._empid = Employee._id_counter

        self._department = None # Internal placeholder before setting
        self.set_empname(empname)
        self.set_salary(salary)
        self.set_address(address)
        self.set_department(department)

    # Magic methods to allow storing Employee objects in a Python Set uniquely by empid
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self._empid == other._empid
        return False

    def __hash__(self):
        return hash(self._empid)

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

        # Remove from existing department set if reassigned
        if self._department is not None:
            self._department.remove_employee(self)

        self._department = department

        # Bi-directional sync: Add this employee to the department's set
        self._department.add_employee(self)

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


# ==========================================
# DERIVED CLASSES
# ==========================================

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


# ==========================================
# DRIVER METHOD (UseEmployee)
# ==========================================

def get_or_create_department(departments_dict: dict) -> Department:
    """Helper to reuse an existing department or create a new one."""
    if departments_dict:
        print("\nExisting Departments:")
        for deptid, dept in departments_dict.items():
            print(f" - ID {deptid}: {dept.get_deptname()}")

        use_existing = input("Assign to existing department? (y/n): ").strip().lower()
        if use_existing == 'y':
            target_id = int(input("Enter existing Department ID: "))
            if target_id in departments_dict:
                return departments_dict[target_id]
            else:
                print("Department ID not found. Creating a new department...")

    print("\n-- Enter New Department Details --")
    deptid = int(input("Department ID: "))
    if deptid in departments_dict:
        print("Department ID already exists! Reusing existing department.")
        return departments_dict[deptid]

    deptname = input("Department Name: ")
    location = input("Department Location: ")
    dept = Department(deptid, deptname, location)
    departments_dict[deptid] = dept
    return dept


def UseEmployee():
    employees = []
    departments_dict = {} # Map of deptid -> Department object

    while True:
        print("\n" + "=" * 40)
        print(" EMPLOYEE MANAGEMENT SYSTEM ")
        print("=" * 40)
        print("1. Add Manager")
        print("2. Add Clerk")
        print("3. Add Salesman")
        print("4. Display All Employees")
        print("5. View Employees by Department (Set View)")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice in ["1", "2", "3"]:
            try:
                empname = input("Enter Employee Name: ")
                salary = float(input("Enter Base Salary: "))

                print("\n-- Enter Address Details --")
                street = input("Street: ")
                city = input("City: ")
                pincode = input("Pincode (6 digits): ")
                address = Address(street, city, pincode)

                department = get_or_create_department(departments_dict)

                if choice == "1":
                    perks = float(input("Enter Perks: "))
                    emp = Manager(empname, salary, department, address, perks)
                elif choice == "2":
                    overtime = float(input("Enter Overtime Pay: "))
                    emp = Clerk(empname, salary, department, address, overtime)
                elif choice == "3":
                    commission = float(input("Enter Commission: "))
                    emp = Salesman(empname, salary, department, address, commission)

                employees.append(emp)
                print(f"\n[Success] {emp.__class__.__name__} Created with Auto-Generated ID: {emp.get_empid()}")

            except EmployeeValidationException as eve:
                print(f"\n[Validation Error]: {eve}")
            except ValueError:
                print("\n[Input Error]: Please enter a valid numeric value.")
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "4":
            if not employees:
                print("\nNo employee records found.")
            else:
                print("\n" + "-" * 40)
                for emp in employees:
                    emp.display_details()
                    print("-" * 40)

        elif choice == "5":
            if not departments_dict:
                print("\nNo departments registered yet.")
            else:
                dept_id = int(input("Enter Department ID to view its employees: "))
                if dept_id in departments_dict:
                    departments_dict[dept_id].display_all_department_employees()
                else:
                    print("Department ID not found.")

        elif choice == "6":
            print("\nExiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 6.")


if __name__ == "__main__":
    UseEmployee()