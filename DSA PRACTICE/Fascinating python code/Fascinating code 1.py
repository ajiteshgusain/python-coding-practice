import turtle
import colorsys

# Set up the screen
turtle.bgcolor('black')
turtle.speed(0)
turtle.width(2)

# Generate a vibrant psychedelic spiral
for i in range(300):
    color = colorsys.hsv_to_rgb(i / 300, 1.0, 1.0)
    turtle.pencolor(color)
    turtle.forward(i * 2)
    turtle.right(59) # Splitting angles creates the complex symmetry

turtle.done()
