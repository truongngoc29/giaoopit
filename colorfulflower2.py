#Giáo Ộp IT
from turtle import*
import colorsys as c
Screen().bgcolor("black")
speed(300)
pensize (3)
shape("circle")
def leaf ():
    begin_fill()
    for uo in range (24):
        color(c.hsv_to_rgb(i/6,1,0.5))
        fillcolor (c.hsv_to_rgb(i/6,1,1))
        fd (10)
        rt (3)
        end_fill()
    for down in range (24):
        fd (5)
        lt (3)
    dot (15)
    rt (180)
    for up in range (24):
        fd(10)
        rt (3)
    begin_fill()
    for ci in range(4):
        color(c.hsv_to_rgb(i/6,1,0.5))
        fillcolor(c.hsv_to_rgb(i/6,1,1))
        lt (90)
        circle (20,180)
    end_fill()
    for down in range (24):
        fd(5)
        lt (3)
    rt (180)
    lt (24)
lt (28)
begin_fill()
for i in range (15):
    leaf ()
    color(c.hsv_to_rgb(i/6,1,0.5))
    fillcolor (c.hsv_to_rgb(i/6,1,1))
end_fill()
done()


