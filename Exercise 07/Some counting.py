"""
## Exercise 7: Some Counting - 20 Marks
 
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*

"""
#Write a loop that counts up from 0 to 50 in increments of 1.
# prints on seperate line
print("Counting from 0 to 50 in increments of 1:")
for a in range(0, 51, 1): # assigning the range, and the incriment value
    print(a)# prints on seperate line
# prints on one line for readability
print("\nCounting from 0 to 50 in increments of 1 on same line:")
for a in range(0, 51, 1): # assigning the range, and the incriment value
    print(a,end=" ")# prints on one line for readability

#Write a loop that counts down from 50 to 0 in decrements of 1.
# prints on seperate line
print("\nCounting down from 50 to 0 in decrements of 1:")
for b in range(50, -1, -1):# assigning the range, and the decrement value
    print(b)# prints on seperate line
# prints on one line for readability
print("\nCounting down from 50 to 0 in decrements of 1 on same line:")
for b in range(50, -1, -1):# assigning the range, and the decrement value
    print(b,end=" ")# prints on one line for readability

#Write a loop that counts up from 30 to 50 in increments of 1.
# prints on seperate line
print("\nCounting from 30 to 50 in increments of 1:")
for c in range(30, 51, 1): # assigning the range, and the incriment value
    print(c)# prints on seperate line
# prints on one line for readability
print("\nCounting from 30 to 50 in increments of 1 in same line:")
for c in range(30, 51, 1): # assigning the range, and the incriment value
    print(c,end=" ")# prints on one line for readability

#Write a loop that counts down from 50 to 10 in decrements of 2.
# prints on seperate line
print("\nCounting down from 50 to 10 in decrements of 2:")
for d in range(50, 9, -2):# assigning the range, and the decrement value
    print(d)# prints on seperate line
# prints on one line for readability
print("\nCounting down from 50 to 10 in decrements of 2 on same line:")
for d in range(50, 9, -2):# assigning the range, and the decrement value
    print(d,end=" ")# prints on one line for readability

#Write a loop that counts up from 100 to 200 in increments of 5.
# prints on seperate line
print("\nCounting from 100 to 200 in increments of 1:")
for e in range(100, 201, 5): # assigning the range, and the incriment value
    print(e)# prints on seperate line
# prints on one line for readability
print("\nCounting from 100 to 200 in increments of 1 on same line:")
for e in range(100, 201, 5): # assigning the range, and the incriment value
    print(e,end=" ")# prints on one line for readability



