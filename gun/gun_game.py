from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import datetime
from gun import *


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg = '#7ebfc3')
canv.pack(fill=tk.BOTH, expand=1)
colors2 = ['#b5dfe5', '#437f83', '#a0d2d8', '#5e9fa3', '#d2f1f6']
colors1 = ['#ae215b', '#c1317e']

t1 = Target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun(canv)

def new_game(event=''):
    global t1, screen1
    t1.new_target()
    g1.bullet = 0
    g1.balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    canv.update()
    zzz = 0.03
    t1.live = 1
    
    while t1.live:
        t1.move()
        for b in g1.balls:
            if b.live:
                b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0

                t1.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bullet) + ' выстрелов')
                b.delete()
                t1.delete()
                b.live = 0

        canv.update()
        time.sleep(zzz)
        g1.targetting()
        g1.power_up()
        for i in g1.balls:
            i.delete()
    time.sleep(1)
    canv.delete(screen1)
    screen1 = canv.create_text(400, 300, text='', font='28')
        
    t = datetime.datetime.now()
    dt = 1
    while (datetime.datetime.now() - t).seconds < dt:
        canv.update()
        time.sleep(zzz)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    #canv.delete(gun)

        
    root.after(1, new_game)


new_game()

tk.mainloop()

