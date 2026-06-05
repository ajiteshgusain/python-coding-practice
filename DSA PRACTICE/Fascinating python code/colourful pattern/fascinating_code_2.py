from turtle import *
import colorsys 

speed(0)
bgcolor('black')
hue=0.0
for i in range(130):
    color_rgb=colorsys.hsv_to_rgb(hue, 1, 1)
    color(color_rgb)

    hue +=0.005

    begin_fill()

    circle(149,90)

    lt(100)


    circle(149 , 90)
    
    end_fill()

done()