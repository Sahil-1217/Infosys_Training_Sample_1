"""
Project 1: Employee Management System
Features:
- Parameterized Constructor
- Getter and Setter Methods
- Custom Exception Raising & Handling
- Inheritance: Base (Employee) -> Derived (Manager, Clerk, Salesman)
- Association: Department and Address classes
- Auto-generated Employee IDs
- Menu Driver: UseEmployee
"""

import re
from EmployeeValidationException import *
from Employee import *
from Manager import *
from Clerk import *
from Salesman import *
from Department import *
from Address import *

def UseEmployee():
    employees = []

    while True:
        print("\n" + "=" * 40)
        print("      EMPLOYEE MANAGEMENT SYSTEM      ")
        print("=" * 40)
        print("1. Add Manager")
        print("2. Add Clerk")
        print("3. Add Salesman")
        print("4. Display All Employees")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice in ["1", "2", "3"]:
            try:
                empname = input("Enter Employee Name: ")
                salary = float(input("Enter Base Salary: "))

                print("\n-- Enter Address Details --")
                street = input("Street: ")
                city = input("City: ")
                pincode = input("Pincode (6 digits): ")
                address = Address(street, city, pincode)

                print("\n-- Enter Department Details --")
                deptid = int(input("Department ID: "))
                deptname = input("Department Name: ")
                location = input("Department Location: ")
                department = Department(deptid, deptname, location)

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
            print("\nExiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please select between 1 and 5.")


if __name__ == "__main__":
    UseEmployee()