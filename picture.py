from graph import *
import time
import random
import math

def keyPressed(event):
    global Dx, Dy, light
    Dx = 0; Dy = 0
    if event.keycode == VK_ESCAPE:
        close()
    elif event.keycode == VK_LEFT:
        Dx = -5
        Dy = 0
    elif event.keycode == VK_RIGHT:
        Dx = 5
        Dy = 0
    elif event.keycode == VK_UP:
        Dx = 0
        Dy = -5
    elif event.keycode == VK_DOWN:
        Dx = 0
        Dy = 5
    elif event.keycode == VK_SPACE:
        turnlights()
    else:
        pass
    move_ghost()
    
def ellips(xc, yc, a, b, fi = 0):
    l=[]
    for x in range(-a, a):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        l.append((xc + math.cos(fi) * x + math.sin(fi) * y, \
                  (yc - math.sin(fi) * x + math.cos(fi) * y)))
    for x in range(a, -a, -1):
        y = ((1 - x**2 / a**2) * b**2) ** (1/2)
        l.append((xc + math.cos(fi) * x + math.sin(fi) * (-y), \
                  (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    polygon(l)

def ellipse(xc, yc, a1, b1, a2, b2, fi = 0):
    l=[]
    if b1<0:
        for x in range(-a1, a1, 5):
            y = ((1 - x**2 / a2**2) * b1**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * (-y), \
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
        for x in range(a2, -a2, -5):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * (-y), \
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    elif b2<0:
        for x in range(a1, -a1, -1):
            y = ((1 - x**2 / a1**2) * b1**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * y, \
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
        for x in range(-a2, a2):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * y, \
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
    else:
        for x in range(a1, -a1, -1):
            y = ((1 - x**2 / a1**2) * b1**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * y, \
                      (yc - math.sin(fi) * x + math.cos(fi) * y)))
        for x in range(-a2, a2):
            y = ((1 - x**2 / a2**2) * b2**2) ** (1/2)
            l.append((xc + math.cos(fi) * x + math.sin(fi) * (-y), \
                      (yc - math.sin(fi) * x + math.cos(fi) * (-y))))
    polygon(l)

def move_ghost():
    global x, Dx, Dy, y
    global head, body, eye1, eye2
    brushColor('lightgray')
    moveObjectBy(head, Dx, Dy)
    moveObjectBy(body, Dx, Dy)
    brushColor('black')
    moveObjectBy(eye1, Dx, Dy)
    moveObjectBy(eye2, Dx, Dy)
    brushColor('white')
    moveObjectBy(blood, Dx, Dy)
    x += Dx
    y += Dy

def windows(r, g, b):
    for i in range(3):
        delta = random.randint(0, 100)
        brush_color = brushColor(r - delta, g - delta, b - delta)
        rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70), 330, \
              100 + (300 - 210) / 4 + i * ((300 - 210)/4 + 70) + 70, 400)

def turnlights():
    global window, light
    if light:
        brushColor('black')
    else:
        brushColor('gold')
    for i in range(3):
        deleteObject(window[i])
        window[i] = rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70), 330, \
              100 + (300 - 210) / 4 + i * ((300 - 210)/4 + 70) + 70, 400)
    light = not light 
    ghostrearm()
    return

def ghostrearm(): #перезагрузка призрака
    global head, body, eye1, eye2, x, y, blood, light
    deleteObject(head)
    deleteObject(eye1)
    deleteObject(body)
    deleteObject(eye2)
    deleteObject(blood)
    brushColor('lightgray')
    head = circle(x, y, 30)
    body = polygon([(x - 60, y + 50), (x - 30, y), (x + 30, y), (x + 60, y + 50)])
    if light:
        brushColor('black')
    else:
        brushColor('red')
    eye1=circle(x - 15, y - 10, 3)
    eye2=circle(x + 15, y - 10, 3)
    if light:
        brushColor('lightgray')
        penColor('lightgray')
    else:
        brushColor('red')
        penColor('red')
    blood = polygon([(x+5,y+1),(x+8,y+1),(x+8,y+11),(x+5,y+11)])
    penColor('black')
    return


def tobase():
    brushColor('black')
    penColor('black')


def updmoon():
    global b1, b2, moon
    deleteObject(moon)
    if b2 == 50 and b1 > -50:
        b1 -= 1
    elif b1 == -50 and b2 == 50:
        b1, b2 = b2, b1
    elif b1 == 50 and b2 < 50:
        b2 += 1
    brushColor('black')
    penColor('light yellow')
    moon = ellipse(430, 50, 50, b1, 50, b2, math.pi/2)
    
light = True
width = 600
height = 600
Dx = 0
Dy = 0
r = 20
g = 55
b = 70
b1 = 50
b2 = 50
brushColor(r, g, b)
rectangle (0, 0, width, height)

#Gradient
for i in range(height):
    penColor(r, g, b)
    line(0, i, 600, i)
    if i % 10 == 0:
        r += 3
        g += 1
        b += 2
brushColor(35, 25, 15)
rectangle(0, 400, 600, 600)

#Moon
brushColor('light yellow')
penColor('light yellow')
moon = ellipse(430, 50, 50, 50, 50, 50, math.pi/2)
brushColor(35, 60, 80)
penColor(brushColor())
tobase()
#Stars
for i in range(300):
    point(random.randint(0, 600), random.randint(0, 400), 'white')

#Clouds
for i in range(10):
    brushColor(115 + i, 100 + 2*i, 145 + 2*i)
    penColor(brushColor())
    l = random.randint(40, 120)
    ellips(random.randint(0, 500), random.randint(0, 350), l, l/4)

#House
penColor('black')
brushColor(37, 30, 20)
rectangle(100, 200, 400, 500)
brushColor(100, 70, 50)
rectangle(100, 270, 400, 285)
for i in range(20):
    rectangle(100 + i*15, 200, i*15 + 110, 270)
rectangle(100, 200, 400, 205)
brushColor(40, 20, 0)
polygon([(70, 200), (320, 130), (430, 200)])
window = [0]*3
for i in range(3):
    brushColor('gold')
    window[i] = rectangle(100 + (300 - 210) / 4 + i * ((300 - 210) / 4 + 70), 330, \
              100 + (300 - 210) / 4 + i * ((300 - 210)/4 + 70) + 70, 400)


#Ghost
head, body, eye1, eye2, blood = 0, 0, 0, 0, 0
x = 100
y = 430
ghostrearm()
onTimer(updmoon, 100)
onKey(keyPressed)

run()





