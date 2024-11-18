"""
Dictionaries:
Use a dictionary to store information about a person you know.Store their first name,
last name, age, and the city in which they live.

You should have keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.
"""

# Define the dictionary with information
Best_friends_info = {
    "First Name": "Romesa",
    "Last Name": "Wasti",
    "Age": "17",
    "City": "Sharjah"
}

# Print all key-value pairs using .items
for key, value in Best_friends_info.items():
    print(f"{key}: {value}")
