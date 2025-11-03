#Name: Patrick O Jegede
#Date: 11/2/2025
#Course: 110-0903.2025FA
#Description: Looping using turtle graphics creating initials

import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(3)

# add some display options
t.pensize(3)            
t.pencolor("green")    
t.shape("turtle")

# Draw "P"
t.penup()
t.goto(-100, -100)
t.setheading(90)
t.pendown()
t.forward(100)
t.right(90)
for _ in range(18):
    t.forward(5)
    t.right(10)
    
# Draw "J" - Modified position
t.penup()
t.goto(50, 0)  # Changed y-coordinate to -100 to align with P's baseline
t.setheading(270)
t.pendown()
t.forward(75)
t.circle(-25, 180)

# Optional: Add horizontal crossbar to J for better letter recognition
t.penup()
t.goto(25, 3)  # Position for J's crossbar
t.setheading(0)
t.pendown()
t.forward(50)

t.hideturtle()
turtle.done()


