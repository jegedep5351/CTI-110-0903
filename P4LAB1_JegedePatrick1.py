# Name: Patrick O Jegede
# Date: 11/2/2025
# Course: 110-0903.2025FA
# Description: Looping using turtle graphics

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Square and Triangle")
screen.bgcolor("white")

# add some display options
t = turtle.Turtle()
t.pensize(3)            
t.pencolor("green")    
t.shape("turtle")

# Create a turtle
t = turtle.Turtle()
t.speed(3)


# Draw a square
print("Drawing a square...")
for i in range(4):
    t.forward(100)
    t.right(90)

# Move to a new position for the triangle
t.penup()
t.goto(150, 0)
t.pendown()

# add some display options
t = turtle.Turtle()
t.pensize(3)
t.pencolor("green")
t.shape("turtle")

# Draw a triangle
print("Drawing a triangle...")
for i in range(3):
    t.forward(100)
    t.left(120)

# Show the turtle
t.showturtle()

# Keep the window open
screen.exitonclick()