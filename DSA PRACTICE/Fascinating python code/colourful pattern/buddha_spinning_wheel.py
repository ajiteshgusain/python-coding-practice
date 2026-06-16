import turtle
import colorsys

# Setup canvas
screen = turtle.Screen()
screen.bgcolor('black')

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

# Drawing loop
for i in range(400):
    # Generates a shifting neon color palette
    color = colorsys.hsv_to_rgb(i / 100, 1.0, 1.0)
    t.pencolor(color)
    
    # Weird math: glitchy angles create a false 3D tunnel
    t.forward(i * 2)
    t.right(137.5)  # An off-center angle forces a chaotic spiral
    t.forward(i)
    t.right(91)   # Second angle creates the optical interference

turtle.done()
