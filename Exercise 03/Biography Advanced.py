"""
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
"""
# Allowing user to input their information in the dictionary
def Personal_User_Information():
    User_Information = {}

    # User input for the full name
    User_Information["Name"] = input("Enter full name: ")

    # User input for hometown
    User_Information["Hometown"] = input("Enter your hometown: ")

    # User input for age with validation using if-else
    while True:
        age_user_input = input("Enter your age: ")
        if age_user_input.isdigit():  # Check if input is numeric
            User_Information["Age"] = int(age_user_input)  # Convert to integer
            break
        else:
            print("Invalid age. Please enter a numeric value.")

    return User_Information

# Merging dictionary with user inputs to print output
User_Information = Personal_User_Information()
print(f"\nName: {User_Information['Name']}\nHometown: {User_Information['Hometown']}\nAge: {User_Information['Age']}")
