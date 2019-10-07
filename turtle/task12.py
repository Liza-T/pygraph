import turtle as t
import math

n = 100
t.shape('turtle')
t.speed(30)
t.left(270)



def duga(radius, angle):
    for i in range (n*angle//360):
        t.forward(2*math.pi*radius/n)
        t.left(3.6)

def smile(radius):
    t.color('gold')
    t.begin_fill()
    duga(radius, 360)
    t.end_fill()
    #radius*=2
    x = t.xcor()
    y = t.ycor()
    t.goto(x+2*radius/5, y+radius/5)
    t.color('DeepSkyBlue3')
    t.begin_fill()
    duga(radius/5, 360)
    t.end_fill()
    t.penup()
    t.goto(x+6*radius/5, y+radius/5)
    t.pendown()
    t.color('DeepSkyBlue3')
    t.begin_fill()
    duga(radius/5, 360)
    t.end_fill()
    t.penup() 
    t.goto(x+radius, y)
    t.pendown()
    t.color('black')
    t.forward(2*radius/5)
    t.penup()
    t.goto(x+2*radius/5, y-radius/5.5)
    t.pendown()
    t.width(5)
    t.color('tomato')
    duga(3*radius/5, 180)

smile(50)












    
