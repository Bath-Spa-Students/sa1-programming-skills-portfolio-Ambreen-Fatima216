"""
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""
# Assigning the correct password
Correct_Password = "12345"
trys = 0  # trys increment initially

# while loop to allow 5 attempts
while trys < 5:
    Password = input("Enter password:")  # Gets user to enter password

    # if statement to check if password is correct
    if Password == Correct_Password:
        print("Correct password")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password, Try again")
    
    # trys increment counter
    trys = trys + 1  # increment counter by 1

# output if all failed attempts
if trys == 5:
    print("Too many incorrect tries. Authorities have been informed.")

