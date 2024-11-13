"""
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
"""
#List of names 
Name_list = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
#Name to search for
Searching_name = "Sam"

# IF to check if the value "Sam" is in the list
# IF and Else statement to check if the value is in the list and print output accordingly
if Searching_name in Name_list:
    print(f"{Searching_name} is found in the list.")
else:
    print(f"{Searching_name} not found in the list.")