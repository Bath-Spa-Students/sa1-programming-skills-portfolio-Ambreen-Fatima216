"""
Control Structures:
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien's color is green. If it is, print a message
that the player just earned 5 points.
"""
# Assigning the alien's colour
Alien_color = "Red"

#Checking using IF function if the aliens colour is Red
if Alien_color.lower() == "red":
    print("You earned +5 points.")

"""•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)
"""
# Assigning the alien's colour
Alien_color = "Red"

#Checking using IF function if the aliens colour is Red
if Alien_color.lower() == "yellow":
    print("You earned +5 points.")
