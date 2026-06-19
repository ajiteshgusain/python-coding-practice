import turtle
import colorsys

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Kaleidoscope")

# Setup the turtle
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.width(2)
t.hideturtle()

def draw_petal(t, size):
    """Draws a single curved petal shape."""
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)
    t.left(120)

# Parameters
num_shapes = 12
angle = 360 / num_shapes

# Drawing the kaleidoscope
for i in range(num_shapes):
    # Dynamic color cycling
    hue = i / num_shapes
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    
    # Draw the shape
    draw_petal(t, 100)
    
    # Rotate for the next shape
    t.right(angle)

turtle.done()