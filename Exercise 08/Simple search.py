"""
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

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
