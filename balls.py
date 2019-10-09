import tkinter as tk
from random import randrange as rnd, choice, randint
import time
import math
root = tk.Tk()
root.geometry('800x600')

canv = tk.Canvas(root, bg = '#7ebfc3')
canv.pack(fill = tk.BOTH, expand = 1)

colors = ['#b5dfe5', '#497f8b', '#a0d2d4', '#5e9fa3', '#d2f1f6']
is_random = True


def new_ball():
    global x, y, r, coords, balls
    #canv.delete(tk.ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    color = choice(colors)
    coords.append([x, y, r, color]) # Цвет - тоже координата! len(coords[i]) = 4
    balls.append(canv.create_oval(x - r, y - r, x + r, y + r, fill = color, width = 0))
    

def move_ball():
    global dr, coords, balls, angle
    canv.delete(tk.ALL)
    for i in range(len(balls) - 1, -1, -1):
        x = coords[i][0]
        y = coords[i][1]
        r = coords[i][2]
        if (y - r <= 0) or (y + r >= 600):
            angle[i] = 360 - angle[i]
        elif (x - r <= 0) or (x + r >= 800):
            angle[i] = 180 - angle[i]
        coords[i][0] = x + dr * math.cos(angle[i] / 57.3)
        coords[i][1] = y + dr * math.sin(angle[i] / 57.3)
        x = coords[i][0]
        y = coords[i][1]
        r = coords[i][2]
        canv.create_oval(x - r, y - r, x + r, y + r, fill = coords[i][3], width = 0)
        
    root.after(15, move_ball)
        

def click(event):
    k = -1
    for i in range(len(coords)):
        if ((coords[i][0] - event.x) ** 2 + (coords[i][1] - event.y) ** 2) ** (1 / 2) <= coords[i][2]:
            k = i
    if k >= 0:
        canv.delete(balls[k])
        balls.pop(k)
        coords.pop(k)
        new_ball()
        is_random = True

dr = 2
coords = []
balls = []
angle = [randint(0, 360) for i in range(10)]
for i in range(10):
    new_ball()
move_ball()
canv.bind('<Button-1>', click)
tk.mainloop()

