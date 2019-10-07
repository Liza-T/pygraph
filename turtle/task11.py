import turtle as t
import math

n = 100
t.shape('turtle')
t.speed(30)
t.left(180)
t.penup()
t.forward(200)
t.pendown()
t.right(90)

def halfcircle(radius):
    for i in range (n//2):
        t.forward(2*math.pi*radius/n)
        t.right(3.6)

number=8
for i in range(number):
    halfcircle(50)
    halfcircle(10)
