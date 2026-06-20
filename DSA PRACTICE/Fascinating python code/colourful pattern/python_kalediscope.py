# # import turtle
# # import colorsys

# # # Setup screen
# # screen = turtle.Screen()
# # screen.setup(800, 800)
# # screen.bgcolor("black")
# # screen.tracer(0)  # Turns off animation for instant drawing

# # t = turtle.Turtle()
# # t.hideturtle()
# # t.speed(0)

# # def draw_leaf(t, size):
# #     """Draws a 'leaf' shape using two arcs."""
# #     t.begin_fill()
# #     t.circle(size, 80)
# #     t.left(100)
# #     t.circle(size, 80)
# #     t.end_fill()

# # # Complexity Parameters
# # num_layers = 5       # How many rings of petals
# # petals_per_layer = 12 # Symmetry factor
# # hue_step = 0.05      # Color shift speed

# # # Generate the Kaleidoscope
# # for layer in range(num_layers):
# #     size = 40 + (layer * 20)  # Each layer gets bigger
# #     for i in range(petals_per_layer):
# #         # Color math for an organic, natural look
# #         hue = (layer / num_layers) + (i / petals_per_layer)
# #         color = colorsys.hsv_to_rgb(hue % 1, 0.7, 0.9)
# #         t.fillcolor(color)
# #         t.pencolor("white")
        
# #         # Positioning
# #         t.penup()
# #         t.goto(0, 0)
# #         t.setheading(i * (360 / petals_per_layer) + (layer * 10))
# #         t.forward(layer * 15) # Offset layers from center
# #         t.pendown()
        
# #         draw_leaf(t, size)

# # screen.update() # Renders the entire drawing at once
# # turtle.done()



# import turtle
# import colorsys

# # Setup screen
# screen = turtle.Screen()
# screen.setup(800, 800)
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.hideturtle()

# # Yahan speed set ki hai (1 sabse slow hai, 10 fast, 0 instantaneous)
# t.speed(3) 
# t.width(2)

# def draw_leaf(t, size):
#     """Draws a 'leaf' shape."""
#     t.begin_fill()
#     t.circle(size, 80)
#     t.left(100)
#     t.circle(size, 80)
#     t.end_fill()

# # Parameters
# num_layers = 5
# petals_per_layer = 12

# # Generate the Kaleidoscope
# for layer in range(num_layers):
#     size = 40 + (layer * 20)
#     for i in range(petals_per_layer):
#         # Color math
#         hue = (layer / num_layers) + (i / petals_per_layer)
#         color = colorsys.hsv_to_rgb(hue % 1, 0.7, 0.9)
#         t.fillcolor(color)
#         t.pencolor("white")
        
#         # Positioning
#         t.penup()
#         t.goto(0, 0)
#         t.setheading(i * (360 / petals_per_layer) + (layer * 10))
#         t.forward(layer * 15)
#         t.pendown()
        
#         draw_leaf(t, size)

# # turtle.done()