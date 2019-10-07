import turtle as t
import math

n = 100
t.shape('turtle')
t.speed(50)
t.right(90)

def circle(m, radius):
    for i in range (n):
        t.forward(2*math.pi*radius/n)
        if m == 0:
            t.left(3.6)
        else:
            t.right(3.6)
r=30
delta_r=10
number = 20
for i in range(number):
    circle(i%2, r)
    if i%2 == 1:
        r+=delta_r
