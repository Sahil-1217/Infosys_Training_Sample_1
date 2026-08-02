"""
Project 2: Banking Management System
Features:
- Parameterized Constructor
- Member Methods
- Centralized Validations & Custom Exceptions
- Base Class: Account (accid, balance, customer, deposit, withdraw)
- Derived Classes: SavingsAccount (minbalance), CurrentAccount (overdraft)
- Association: Customer (custid, custname, address, accounts), Address (street, city, pincode)
- Auto-generated Account and Customer IDs
- Driver Application: UseBankingApp
"""

import re
from Saving_Account import *
from Current_Account import *
from Customer import *
from Address import *


def UseBankingApp():
    accounts_list = []

    while True:
        print("\n" + "=" * 40)
        print("       BANKING MANAGEMENT SYSTEM       ")
        print("=" * 40)
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Display All Accounts")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()

        if choice in ["1", "2"]:
            try:
                custname = input("Enter Customer Name: ")

                print("\n-- Enter Address Details --")
                street = input("Street: ")
                city = input("City: ")
                pincode = input("Pincode (6 digits): ")
                address = Address(street, city, pincode)

                # Create Customer
                customer = Customer(custname, address)

                print("\n-- Enter Account Details --")
                balance = float(input("Enter Initial Balance: "))

                if choice == "1":
                    minbalance = float(input("Enter Minimum Balance required (e.g. 1000): "))
                    acc = SavingsAccount(balance, customer, minbalance)
                elif choice == "2":
                    overdraft = float(input("Enter Overdraft Limit (e.g. 5000): "))
                    acc = CurrentAccount(balance, customer, overdraft)

                accounts_list.append(acc)
                print(f"\n[Success] {acc.__class__.__name__} Created with Auto Account ID: {acc.accid}")

            except BankValidationException as bve:
                print(f"\n[Validation Error]: {bve}")
            except ValueError:
                print("\n[Input Error]: Please enter numeric values where required.")
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice in ["3", "4"]:
            if not accounts_list:
                print("\nNo accounts available. Create an account first!")
                continue

            try:
                acc_id = int(input("Enter Account ID: "))
                target_acc = None

                for acc in accounts_list:
                    if acc.accid == acc_id:
                        target_acc = acc
                        break

                if target_acc is None:
                    print("\n[Error]: Account ID not found.")
                else:
                    amt = float(input("Enter Amount: "))
                    if choice == "3":
                        target_acc.deposit(amt)
                    elif choice == "4":
                        target_acc.withdraw(amt)

            except BankValidationException as bve:
                print(f"\n[Validation Error]: {bve}")
            except ValueError:
                print("\n[Input Error]: Please enter a valid number.")

        elif choice == "5":
            if not accounts_list:
                print("\nNo account records found.")
            else:
                print("\n" + "-" * 40)
                for acc in accounts_list:
                    acc.display_account_details()
                    print("-" * 40)

        elif choice == "6":
            print("\nExiting Banking Management System. Goodbye!")
            break

        else:
            print("Invalid choice, please select between 1 and 6.")


if __name__ == "__main__":
    UseBankingApp()