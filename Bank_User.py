from Bank import *

def run_banking_system():
    print("=== Welcome to the Banking Management System ===")
    
    try:
        name = input("Enter Account Holder Name: ")
        acc_type = input("Enter Account Type (Savings / Current): ").strip().lower()
        initial_deposit = float(input("Enter Initial Deposit Amount: "))
        acc_no = random.randint(10000, 99999)
        
        if acc_type == "savings":
            account = SavingsAccount(acc_no, name, initial_deposit)
        elif acc_type == "current":
            account = CurrentAccount(acc_no, name, initial_deposit)
        else:
            print("Unknown selection. Defaulting account initialization to Savings Setup.")
            account = SavingsAccount(acc_no, name, initial_deposit)
            
        print("\n[SUCCESS] Account Created Successfully!")
        print(account.show_details())
        
    except (ValidationError, InvalidTransactionError) as err:
        print(f"\n[REGISTRATION SYSTEM BLOCKED]: {err}")
        return 
    except ValueError:
        print("\n[INPUT ERROR]: Initial deposit field requires valid integer or floating numeric formats.")
        return
    except Exception as general_err:
        print(f"\n[CRITICAL INITIALIZATION ERROR]: Unhandled failure: {general_err}")
        return

    # Non-crashing loop that safely catches everything raised by class functions
    while True:
        try:
            print("\n--- Banking Menu ---")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Show Account Details")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":  
                amt = float(input("Enter amount to deposit: "))
                message = account.deposit(amt)
                print(message)
                
            elif choice == "2": 
                amt = float(input("Enter amount to withdraw: "))
                message = account.withdraw(amt)
                print(message)
                
            elif choice == "3": 
                print("\n--- Current Details ---")
                print(account.show_details())
                
            elif choice == "4":
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice! Please select an execution item between 1 and 4.")
                
        except ValueError:
            print("\n[INPUT FORMAT FAILURE]: Transaction value input fields must be numerical formats.")
        except BankingException as bank_err:
            print(f"\n[BANKING CORE REJECTION]: Operation denied by internal rules -> {bank_err}")
        except Exception as unhandled:
            print(f"\n[SYSTEM HALT ERROR]: Internal run exception caught: {unhandled}")

if __name__ == "__main__":
    run_banking_system()
