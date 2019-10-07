import turtle as t
import math

t.shape('turtle')


l = 2
angle = 7


for i in range (10, 500):
    t.forward(l)
    t.left(angle)
    l+= 0.1
    #angle -= math.log(i, 10) - 1

