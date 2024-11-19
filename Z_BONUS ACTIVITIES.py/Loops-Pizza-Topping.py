"""
Loops- Pizza Toppings :
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you'll add that topping to their pizza.

"""
# Toppings in a list 
print("Enter 'quit' to stop adding toppings.")

while True:
    toppings = input("Enter a topping: ")

    if toppings.lower() == "quit":
        print("No more toppings will be added.")
        break
    else: 
        print(f"I'll add {toppings} to your pizza.")

   