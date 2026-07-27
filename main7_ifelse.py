import random

# Parent Class
class Employee:
    def __init__(self, emp_id, name, salary):
        # 1. Validate Employee ID
        if emp_id <= 0:
            raise ValueError(f"Invalid ID ({emp_id}). Employee ID must be greater than 0!")
        
        # 2. Validate Name (strips whitespace to ensure it's not just spaces)
        if not name or not name.strip():
            raise ValueError("Employee name cannot be blank or empty!")
            
        # 3. Validate Salary
        if salary < 0:
            raise ValueError(f"Invalid Salary (₹{salary}). Salary cannot be negative!")

        self.emp_id = emp_id
        self.name = name.strip()
        self.salary = salary

    def get_details(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Salary: ₹{self.salary}"

# Child Class inheriting from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        
        # Validate Department
        if not department or not department.strip():
            raise ValueError("Department name cannot be blank!")
            
        self.department = department.strip()

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Dept: {self.department}"

class Clerk(Employee):
    def __init__(self, emp_id, name, salary, overTime, Overtime_pay):
        super().__init__(emp_id, name, salary)
        
        # Validate Clerk metrics
        if overTime < 0:
            raise ValueError("Overtime hours cannot be negative!")
        if Overtime_pay < 0:
            raise ValueError("Overtime pay rate cannot be negative!")
            
        self.overTime = overTime
        self.Overtime_pay = Overtime_pay

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Overtime: {self.overTime} hrs | OverTime_Pay: ₹{self.Overtime_pay}"

class SalesMan(Employee):
    def __init__(self, emp_id, name, salary, commsion):
        super().__init__(emp_id, name, salary)
        
        # Validate Commission
        if commsion < 0:
            raise ValueError("Commission payout cannot be negative!")
            
        self.commsion = commsion

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Commision: ₹{self.commsion}"

# --- Execution Code ---
try:
    print("--- Running Valid Registrations ---")
    
    # 1. Create a Manager object 
    Id_Man = random.randint(1, 10)
    mgr1 = Manager(Id_Man, "Sahil Bhoye", 95000, "IT Operations")
    print("Manager Details:")
    print(mgr1.get_details())
    print("-" * 40)

    # 2. Create a SalesMan object 
    Id_Sal = random.randint(21, 30)
    Sal = SalesMan(Id_Sal, "Shivam Bhoye", 105000, 10000)
    print("SalesMan Details:")
    print(Sal.get_details())
    print("-" * 40)

    # 3. Create a Clerk object
    Id_Cle = random.randint(31, 40)
    Cle = Clerk(Id_Cle, "Sai Bhoye", 50000, 5, 10000)
    print("Clerk Details:")
    print(Cle.get_details())
    print("-" * 40)

    # --- Test Triggering a Validation Error ---
    print("\n--- Testing Invalid Data Catching ---")
    # This will immediately jump to the 'except' block below because salary is negative
    broken_emp = Clerk(45, "Bad Data Input", -25000, 0, 0)

except ValueError as error:
    print(f"[VALIDATION ERROR CATCHED]: {error}")
