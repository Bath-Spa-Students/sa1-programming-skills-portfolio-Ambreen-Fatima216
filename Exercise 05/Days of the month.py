"""
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""
#Creating a dictionary to hold the months and the days as values
# Dictionary of months and days
Months_Days = {
    1: 31,   # January
    2: 28,   # February default days
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

# Prompt user to enter a month number
Months = int(input("Enter a month number (1-12): "))

# Check if the month is valid and output the corresponding days
if 1 <= Months <= 12:
    print(f"The month {Months} has {Months_Days[Months]} days.")
else:
    print("Invalid month. Enter a number between 1 and 12.")
