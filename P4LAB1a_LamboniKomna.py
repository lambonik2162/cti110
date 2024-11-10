# Lamboni, Komna
# 11/03/2024
# P4LAB1a
# Use turtle and loops to draw a square and a triangle.

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(8)
pen.pencolor("blue")
pen.shape("arrow")

# Code to draw the shapes
for side in range(4):
    pen.forward(200)
    pen.left(90)

# While loop that executea 3 times
sides = 3
while sides > 0:
    pen.forward(200)
    pen.left(120)
    sides = sides - 1
# Wait for user to close window
win.mainloop()
    



