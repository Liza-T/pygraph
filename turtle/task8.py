import turtle as t
import math

def draw(sides, lenght):
    for i in range(sides):
        t.forward(lenght)
        t.left(360/sides)
def moveright():
    t.penup()
    t.forward(30)
    t.pendown()

def length(sides):
    r = 30 + (sides-3)*30
    a = r*2*math.sin((360/(2*sides))/57.3)
    return(abs(a))

t.speed(10)
t.shape('turtle')
#t.forward(200)
t.left(150)
for i in range (1, 11):
    #t.left(90 + 180/(i+3))
    draw(i+2, length(i+2))
    t.right(90 + 180/(i+2))
    moveright()
    t.left(90 + 180/(i+3))
    
     
