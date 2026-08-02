"""
Case Study 2: Hospital Employee Management System
Features:
- Base Class: HospitalEmployee
- Derived Subclasses: Doctor (OPD/IPD), Nurse, Technician, AdminStaff
- Associated Classes: Department, Address
- Functionalities: Add, Remove, and Generate Detailed Employee Reports
- Concepts: Data Hiding, Simple Getters/Setters, Custom Exceptions, Auto-generated IDs
"""

import re


# ==========================================
# CUSTOM EXCEPTION
# ==========================================

class HospitalValidationException(Exception):
    """Custom exception for validation errors in hospital management."""
    pass


# ==========================================
# ASSOCIATED CLASSES
# ==========================================

class Address:
    """Address Class (Associated with HospitalEmployee)."""

    def __init__(self, street: str, city: str, pincode: str):
        self.set_street(street)
        self.set_city(city)
        self.set_pincode(pincode)

    def get_street(self):
        return self._street

    def set_street(self, street: str):
        if not street or not street.strip():
            raise HospitalValidationException("Street cannot be empty.")
        self._street = street.strip()

    def get_city(self):
        return self._city

    def set_city(self, city: str):
        if not city or not city.strip():
            raise HospitalValidationException("City cannot be empty.")
        self._city = city.strip()

    def get_pincode(self):
        return self._pincode

    def set_pincode(self, pincode: str):
        pincode_str = str(pincode).strip()
        if not re.match(r"^\d{6}$", pincode_str):
            raise HospitalValidationException("Pincode must be exactly 6 digits.")
        self._pincode = pincode_str

    def display_address(self):
        return f"{self._street}, {self._city} - {self._pincode}"


class Department:
    """Department Class (Associated with HospitalEmployee)."""

    def __init__(self, dept_id: int, dept_name: str, floor_no: int):
        self.set_dept_id(dept_id)
        self.set_dept_name(dept_name)
        self.set_floor_no(floor_no)

    def get_dept_id(self):
        return self._dept_id

    def set_dept_id(self, dept_id: int):
        if dept_id <= 0:
            raise HospitalValidationException("Department ID must be greater than zero.")
        self._dept_id = dept_id

    def get_dept_name(self):
        return self._dept_name

    def set_dept_name(self, dept_name: str):
        if not dept_name or not dept_name.strip():
            raise HospitalValidationException("Department Name cannot be empty.")
        self._dept_name = dept_name.strip()

    def get_floor_no(self):
        return self._floor_no

    def set_floor_no(self, floor_no: int):
        if floor_no < 0:
            raise HospitalValidationException("Floor number cannot be negative.")
        self._floor_no = floor_no

    def display_department(self):
        return f"{self._dept_name} (ID: {self._dept_id}, Floor: {self._floor_no})"


# ==========================================
# BASE EMPLOYEE CLASS
# ==========================================

class HospitalEmployee:
    """Base Class for Hospital Employees."""
    hospital_name = "City Care General Hospital"
    _id_counter = 100  # For auto-generating Employee IDs

    def __init__(self, name: str, base_salary: float, department: Department, address: Address):
        HospitalEmployee._id_counter += 1
        self.__emp_id = HospitalEmployee._id_counter  # Data hiding (Private)

        self.set_name(name)
        self.set_base_salary(base_salary)
        self.set_department(department)
        self.set_address(address)

    # Getters and Setters
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not name or not name.strip():
            raise HospitalValidationException("Employee Name cannot be empty.")
        self.__name = name.strip()

    def get_base_salary(self):
        return self.__base_salary

    def set_base_salary(self, base_salary: float):
        if base_salary < 0:
            raise HospitalValidationException("Base salary cannot be negative.")
        self.__base_salary = float(base_salary)

    def get_department(self):
        return self._department

    def set_department(self, department: Department):
        if not isinstance(department, Department):
            raise HospitalValidationException("Invalid Department object.")
        self._department = department

    def get_address(self):
        return self._address

    def set_address(self, address: Address):
        if not isinstance(address, Address):
            raise HospitalValidationException("Invalid Address object.")
        self._address = address

    def calculate_total_salary(self):
        return self.__base_salary

    def generate_report(self):
        """Prints a complete detailed report for the employee."""
        print(f"Hospital Name : {HospitalEmployee.hospital_name}")
        print(f"Employee ID   : {self.__emp_id}")
        print(f"Name          : {self.__name}")
        print(f"Role/Type     : {self.__class__.__name__}")
        print(f"Base Salary   : ${self.__base_salary:.2f}")
        print(f"Total Salary  : ${self.calculate_total_salary():.2f}")
        print(f"Department    : {self._department.display_department()}")
        print(f"Address       : {self._address.display_address()}")


# ==========================================
# DERIVED SUBCLASSES
# ==========================================

class Doctor(HospitalEmployee):
    """Derived Subclass: Doctor (OPD or IPD)."""

    def __init__(self, name: str, base_salary: float, department: Department, address: Address, doctor_type: str, consultation_fee: float):
        super().__init__(name, base_salary, department, address)
        self.set_doctor_type(doctor_type)
        self.set_consultation_fee(consultation_fee)

    def get_doctor_type(self):
        return self._doctor_type

    def set_doctor_type(self, doctor_type: str):
        doc_type = doctor_type.strip().upper()
        if doc_type not in ["OPD", "IPD"]:
            raise HospitalValidationException("Doctor type must be either 'OPD' or 'IPD'.")
        self._doctor_type = doc_type

    def get_consultation_fee(self):
        return self._consultation_fee

    def set_consultation_fee(self, consultation_fee: float):
        if consultation_fee < 0:
            raise HospitalValidationException("Consultation fee cannot be negative.")
        self._consultation_fee = float(consultation_fee)

    def calculate_total_salary(self):
        return self.get_base_salary() + self._consultation_fee

    def generate_report(self):
        super().generate_report()
        print(f"Doctor Category: {self._doctor_type}")
        print(f"Extra Fee/Allowance: ${self._consultation_fee:.2f}")


class Nurse(HospitalEmployee):
    """Derived Subclass: Nurse."""

    def __init__(self, name: str, base_salary: float, department: Department, address: Address, night_shift_allowance: float):
        super().__init__(name, base_salary, department, address)
        self.set_night_shift_allowance(night_shift_allowance)

    def get_night_shift_allowance(self):
        return self._night_shift_allowance

    def set_night_shift_allowance(self, night_shift_allowance: float):
        if night_shift_allowance < 0:
            raise HospitalValidationException("Night shift allowance cannot be negative.")
        self._night_shift_allowance = float(night_shift_allowance)

    def calculate_total_salary(self):
        return self.get_base_salary() + self._night_shift_allowance

    def generate_report(self):
        super().generate_report()
        print(f"Shift Allowance: ${self._night_shift_allowance:.2f}")


class Technician(HospitalEmployee):
    """Derived Subclass: Technician."""

    def __init__(self, name: str, base_salary: float, department: Department, address: Address, lab_allowance: float):
        super().__init__(name, base_salary, department, address)
        self.set_lab_allowance(lab_allowance)

    def get_lab_allowance(self):
        return self._lab_allowance

    def set_lab_allowance(self, lab_allowance: float):
        if lab_allowance < 0:
            raise HospitalValidationException("Lab allowance cannot be negative.")
        self._lab_allowance = float(lab_allowance)

    def calculate_total_salary(self):
        return self.get_base_salary() + self._lab_allowance

    def generate_report(self):
        super().generate_report()
        print(f"Lab Allowance  : ${self._lab_allowance:.2f}")


class AdminStaff(HospitalEmployee):
    """Derived Subclass: Admin Staff."""

    def __init__(self, name: str, base_salary: float, department: Department, address: Address, admin_bonus: float):
        super().__init__(name, base_salary, department, address)
        self.set_admin_bonus(admin_bonus)

    def get_admin_bonus(self):
        return self._admin_bonus

    def set_admin_bonus(self, admin_bonus: float):
        if admin_bonus < 0:
            raise HospitalValidationException("Admin bonus cannot be negative.")
        self._admin_bonus = float(admin_bonus)

    def calculate_total_salary(self):
        return self.get_base_salary() + self._admin_bonus

    def generate_report(self):
        super().generate_report()
        print(f"Admin Bonus    : ${self._admin_bonus:.2f}")


# ==========================================
# HELPER INPUT FUNCTION
# ==========================================

def get_common_inputs():
    """Helper function to collect name, base salary, address, and department."""
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Base Salary: "))

    print("\n-- Enter Address Details --")
    street = input("Street: ")
    city = input("City: ")
    pincode = input("Pincode (6 digits): ")
    address = Address(street, city, pincode)

    print("\n-- Enter Department Details --")
    dept_id = int(input("Department ID: "))
    dept_name = input("Department Name (e.g. Cardiology, OPD, ICU, Radiology): ")
    floor_no = int(input("Floor Number: "))
    department = Department(dept_id, dept_name, floor_no)

    return name, salary, department, address


# ==========================================
# DRIVER APPLICATION
# ==========================================

def UseHospitalApp():
    employees = []

    while True:
        print("\n" + "=" * 50)
        print(f"   {HospitalEmployee.hospital_name.upper()}   ")
        print("   HOSPITAL EMPLOYEE MANAGEMENT SYSTEM   ")
        print("=" * 50)
        print("1. Add New Doctor (OPD / IPD)")
        print("2. Add New Nurse")
        print("3. Add New Technician")
        print("4. Add New Admin Staff")
        print("5. Remove Employee by ID")
        print("6. Generate All Employee Detailed Report")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice in ["1", "2", "3", "4"]:
            try:
                name, salary, department, address = get_common_inputs()

                if choice == "1":
                    doc_type = input("Enter Doctor Category (OPD/IPD): ")
                    fee = float(input("Enter Consultation Fee / Allowance: "))
                    emp = Doctor(name, salary, department, address, doc_type, fee)

                elif choice == "2":
                    allowance = float(input("Enter Night Shift Allowance: "))
                    emp = Nurse(name, salary, department, address, allowance)

                elif choice == "3":
                    lab_allowance = float(input("Enter Lab Hazard Allowance: "))
                    emp = Technician(name, salary, department, address, lab_allowance)

                elif choice == "4":
                    bonus = float(input("Enter Admin Bonus: "))
                    emp = AdminStaff(name, salary, department, address, bonus)

                employees.append(emp)
                print(f"\n[Success] {emp.__class__.__name__} Added! Auto Employee ID: {emp.get_emp_id()}")

            except HospitalValidationException as hve:
                print(f"\n[Validation Error]: {hve}")
            except ValueError:
                print("\n[Input Error]: Please enter valid numerical values where required.")
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "5":
            if not employees:
                print("\nNo employee records to delete.")
                continue

            try:
                emp_id = int(input("Enter Employee ID to remove: "))
                found = False

                for emp in employees:
                    if emp.get_emp_id() == emp_id:
                        employees.remove(emp)
                        print(f"\n[Success] Employee with ID {emp_id} removed successfully.")
                        found = True
                        break

                if not found:
                    print("\n[Error]: Employee ID not found.")

            except ValueError:
                print("\n[Input Error]: Please enter a valid numerical ID.")

        elif choice == "6":
            if not employees:
                print("\nNo employee records found.")
            else:
                print("\n" + "*" * 50)
                print("           FULL EMPLOYEE MANAGEMENT REPORT          ")
                print("*" * 50)
                for emp in employees:
                    emp.generate_report()
                    print("-" * 50)

        elif choice == "7":
            print("\nExiting Hospital Employee Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select an option between 1 and 7.")


if __name__ == "__main__":
    UseHospitalApp()