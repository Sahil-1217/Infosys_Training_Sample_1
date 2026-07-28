import math
try:
    var1 = int(input("Enter the Number bro::::"))
    if var1 <0:
        print("Number is Negative !!!!!!")
    elif var1==0:
        print("Number is Zero!!!!!")    
    else:
        print("NUmber is Positive!!!")
        if var1 % 2 == 0:
            print("The Number is Even!!!!!!") 
            if var1 == 2:
                print("Its a Prime number 2!!!!")   
        else:
            print("The number is oDD!!!!")  
            # 2. Check Prime Number Logic
            is_prime = True
            
            if var1 < 2:
                is_prime = False
            elif var1 == 2:
                is_prime = True
            elif var1 % 2 == 0:
                is_prime = False  # Even numbers greater than 2 are not prime
            else:
                # Check odd numbers up to the square root
                limit = int(math.sqrt(var1)) + 1
                for i in range(3, limit, 2):
                    if var1 % i == 0:
                        is_prime = False
                        break  # Stop checking if we find a factor

            # 3. Print Prime Results
            if is_prime:
                print("The number is Prime !!!!!")
            else:
                print("The number is not Prime  !!!!!!")
except Exception as e:
    print(f"The Exception is : {e}")                
    
       
                
          


# name = input("Enter the name of User :")
# age = int(input("ENter the age of USer :::"))
# try:

#     if age < 0:
#         print("The age should not be Negative!!!")
#     elif age == 0:
#         print("Age is Zero Not valid !!!!")    
#     elif age < 18:
#         raise ValueError("These user cannot Vote , not Eligible for vote")
#     else:
#         print("Yes Eligible for Vote:")
# except Exception as e:
#     print(f"Exceprion is {e}")        



# import math

# try:
#     var1 = int(input("Enter the Number bro::::"))

#     if var1 < 0:
#         print("Number is Negative !!!!!!")
#     elif var1 == 0:
#         print("Number is Zero!!!!!")    
#     else:
#         print("Number is Positive!!!")
        
#         # 1. Check Even or Odd
#         if var1 % 2 == 0:
#             print("The Number is Even!!!!!!")    
#         else:
#             print("The number is oDD!!!!")  
        
#         # 2. Check Prime Number Logic
#         is_prime = True
        
#         if var1 < 2:
#             is_prime = False
#         elif var1 == 2:
#             is_prime = True
#         elif var1 % 2 == 0:
#             is_prime = False  # Even numbers greater than 2 are not prime
#         else:
#             # Check odd numbers up to the square root
#             limit = int(math.sqrt(var1)) + 1
#             for i in range(3, limit, 2):
#                 if var1 % i == 0:
#                     is_prime = False
#                     break  # Stop checking if we find a factor

#         # 3. Print Prime Results
#         if is_prime:
#             print("The number is Prime !!!!!")
#         else:
#             print("The number is not Prime  !!!!!!")

# except ValueError:
#     print("Bro, that's not a valid number! Please enter integers only!")
