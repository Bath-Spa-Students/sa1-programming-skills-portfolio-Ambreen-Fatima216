"""
Write a program that tests if a value is even or odd. Follow the instructions outlined below:  

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd. 
* The message returned by the function should be printed from within the main function.
"""
# Function to check whether the number is odd or even(Concepy for this learned from:https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#:~:text=Also%2C%20if%E2%80%A6else%20statements%20will,required%20code%20is%20provided%20below.&text=num%20%3D%20int%20(input%20(%E2%80%9C,even%3A%20887%20887%20is%20odd. )
def odd_even_check(number):
    if (number % 2) == 0:
        print("The number is even")  # Print even message
    else:
        print("The provided number is odd")  # Print odd message

# Main function 
def main():
    # user input for a number
    number = int(input("Enter a number:"))
    #using the function to print the output
    odd_even_check(number)  # Call the function and it will print the result
