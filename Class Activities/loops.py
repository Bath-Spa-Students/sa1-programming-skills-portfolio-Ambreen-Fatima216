#loops
#types of loop
"""
1.While loop
2.Why loop
3.For loop
"""
#practice one
b = 2
while b < 10:
  print(b)
  b= b+1

#practice two
count = 2
while count <= 10:
    print("Count is:", count)
    count += 1

#practice three infinite loops with break
a = 2
while a < 9:
  print(a)
  if a == 3:
    break
  a= a+1  

 #For loop 
  ''''A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

#For loop practice
Cities = ["NYC", "LA", "San Franscisco"]
for c in Cities:
  print(c)

# Using the range Function with the for Loop

  for a in range(0,30):
      print (a)

for a in range(20):
     print (a)

# To improve readibility by printing output in one line

for v in range(0,20):
 print (v, end=",")# using commas to seperate

for x in range(0,25):
 print (x, end=" ")# using space to seperate 

#Step count to create incriments

for h in range (0,27,2):    # Count +2 
   print(h ,end=",")

# Count +5
for l in range (0,12,5):
      print(l,end=",")
