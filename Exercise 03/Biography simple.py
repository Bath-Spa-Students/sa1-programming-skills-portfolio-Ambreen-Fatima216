"""## Exercise 3: Biography - 25 Marks

In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information."""

#Storing information inside dictionaries
Personal_Information = {
    'name': 'Ambreen Fatima Naqvi',  # Name Key Variable
    'hometown': 'Sharjah, UAE',  # Hometown Key variable
    'age': 17  #Age Key variable
}
print("Name: " + Personal_Information['name'] + "\nHometown: " + Personal_Information['hometown'] + "\nAge: " + str(Personal_Information['age']))
