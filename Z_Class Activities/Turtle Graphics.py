#Turtle graphics to print a red heart
import turtle

# Setting up the turtle
turtle = turtle.Turtle()
turtle.speed(2)
turtle.color("red")

# Start drawing the heart
turtle.begin_fill()
turtle.left(50)
turtle.forward(100)
turtle.circle(50, 180)
turtle.right(100)
turtle.circle(50, 180)
turtle.forward(100)
turtle.end_fill()

# Keep the window open
turtle.done()
