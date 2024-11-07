"""
In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
"""
print("What are the capitals of the following European Countries")

#Asks the user the Question about the Captital of France
print("What is the capital of France?")
Answer = input("Your answer: ")
# First check for the correct answer
if Answer.lower() == "paris":
    print("Your answer is correct +1 points")
else:
    # Using nested if to let the user have another try
    print("Your answer is incorrect. Try again")
    Answer = input("Your answer: ")

    if Answer.lower() == "paris":
        print("Correct! Well done.")
    else:
        print("Still incorrect. The correct answer is Paris.")
