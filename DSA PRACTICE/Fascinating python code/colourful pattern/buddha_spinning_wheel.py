import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
wheel = turtle.Turtle()
wheel.speed(0)  # Fastest speed
wheel.width(2)

# Define colors for the pattern
colors = ["#FFD700", "#DAA520", "#B8860B"] # Shades of gold/yellow

def draw_petal(t, size):
    """Draws a single petal shape."""
    t.color("gold")
    t.begin_fill()
    t.circle(size, 60)  # Draw arc
    t.left(120)         # Turn to close the shape
    t.circle(size, 60)  # Draw arc
    t.left(120)         # Turn to close the shape
    t.end_fill()

# Draw the pattern
for i in range(12):  # Creating 12 spokes
    wheel.penup()
    wheel.goto(0, 0)
    wheel.pendown()
    wheel.right(i * 30)  # Rotate 30 degrees each time (360/12 = 30)
    wheel.forward(50)    # Move away from center
    draw_petal(wheel, 60)

# Hide the turtle and keep the window open
wheel.hideturtle()
turtle.done()