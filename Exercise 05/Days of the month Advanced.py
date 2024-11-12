"""
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

"""
# Code edited to fit the advanced requirements
# Dictionary of months and days
Months_Days = {
    1: 31,   # January
    2: 28,   # February default days later adjusted for leap years
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# User input for month number
Months = int(input("Enter a month number (1-12): "))

# Checking if the month is a valid number and corresponding days  
if 1 <= Months <= 12:
    if Months == 2:
        Leap_Year = input("Is it a leap year? (Yes/No): ").lower()  

        # Set days to 29 if leap year otherwise it stays default
        Days = 29 if Leap_Year == "yes" else Months_Days[Months]
    else:
        Days = Months_Days[Months]

    # Print the number of days corresponding to the month 
    print(f"The month {Months} has {Days} days.")
else:
    print("Invalid month. Enter a number between 1 and 12.")

