import tkinter as tk
from random import randrange as rnd, choice
import math

root = tk.Tk()
root.geometry('800x600')
canv = tk.Canvas(root, bg='#7ebfc3')
canv.pack(fill=tk.BOTH, expand=1)

colors2 = ['#b5dfe5', '#437f83', '#a0d2d8', '#5e9fa3', '#d2f1f6']
colors1 = ['#ae215b', '#c1317e']
delta_t = 5
score = 0
balls_number1 = 5
balls_number2 = 10


class Ball():

    def __init__(self, r, color):
        self.x = rnd(0 + r, 800 - r)
        self.y = rnd(0 + r, 600 - r)
        self.r = r
        self.color = color
        self.obj = canv.create_oval(
                        self.x - r, self.y - r,
                        self.x + r, self.y + r,
                        fill=color, width=0
                        )

    def delete(self):
        canv.delete(self.obj)

    def draw_ball(self):
        self.obj = canv.create_oval(
                        self.x - self.r, self.y - self.r,
                        self.x + self.r, self.y + self.r,
                        fill=self.color, width=0
                        )

    def reflection(self):
        if self.x - self.r < 0 and self.vx < 0:
            self.x += (self.r - self.x)
            self.vx = -self.vx
        elif self.x + self.r > 800 and self.vx > 0:
            self.x -= (self.x + self.r - 800)
            self.vx = -self.vx
        elif self.y - self.r < 0 and self.vy > 0:
            self.y += (self.r - self.y)
            self.vy = -self.vy
        elif self.y + self.r > 600-20 and self.vy < 0:
            self.y -= (self.y + self.r - 600+20)
            self.vy = -self.vy

    def collision(self, other):
        m1 = self.r**2
        m2 = other.r**2
        dist = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        cos_fi = (self.x - other.x) / dist
        sin_fi = abs((self.y - other.y) / dist)
        vx10 = self.vx * cos_fi + self.vy * sin_fi
        vx20 = other.vx * cos_fi + other.vy * sin_fi
        vy1 = self.vy * cos_fi + self.vx * (-sin_fi)
        vy2 = other.vy * cos_fi + other.vx * (-sin_fi)
        vx1 = 2 * vx20 * m2 / (m1 + m2) - vx10 * (m2 - m1) / (m2 + m1)
        vx2 = 2 * vx10 * m1 / (m1 + m2) - vx20 * (m2 - m1) / (m2 + m1)
        if cos_fi**2 != sin_fi**2:
            self.vx = ((vy1 * sin_fi - vx1 * cos_fi) /
                    (sin_fi**2 + cos_fi**2))
            self.vy = ((vy1 * cos_fi - vx1 * sin_fi) /
                    (cos_fi**2 + sin_fi**2))
        else:
            self.vx = 0
            self.vy = 0
        self.vx = vx1 * cos_fi + vy1 * sin_fi
        other.vx = vx2 * cos_fi + vy2 * sin_fi
        self.vy = vy1 * cos_fi + vx1 * sin_fi
        other.vy = vy2 * cos_fi + vx2 * sin_fi
        delta_r = (self.r + other.r) / dist
        self.x += delta_r * (self.x - other.x) / dist
        self.y += delta_r * (self.y - other.y) / dist


class Ball1(Ball):

    def __init__(self, r, color):
        super().__init__(r, color)
        self.vx = rnd(0, 80)/20
        self.vy = rnd(0, 80)/20
        self.dt = 1

    def move_ball1(self):
        self.delete()
        a = 0.04
        self.x += self.vx * self.dt
        self.y += -(self.vy * self.dt - a * self.dt ** 2 / 2)
        self.vy -= a * self.dt
        self.reflection()
        self.draw_ball()


class Ball2(Ball):

    def __init__(self, r, color):
        super().__init__(r, color)
        self.vx = rnd(0, 55)/20
        self.vy = rnd(0, 55)/20

    def move_ball2(self):
        self.delete()
        self.reflection()
        self.x += self.vx
        self.y -= self.vy
        self.draw_ball()


def click(event):
    global score, l
    k = -1
    for i in range(len(balls)):
        if (
                (balls[i].x - event.x)**2 +
                (balls[i].y - event.y)**2)**0.5 <= balls[i].r:
            k = i
    if k >= 0:
        canv.delete(balls[k].obj)
        balls[k].x = rnd(100, 700)
        balls[k].y = rnd(100, 500)
        if type(balls[k]) == Ball2:
            score += 1
            balls[k].r = rnd(30, 50)
            balls[k].color = choice(colors2)
            balls[k].vx = rnd(0, 50) / 20
            balls[k].vy = rnd(0, 50) / 20
        else:
            score += 10
            balls[k].r = rnd(7, 15)
            balls[k].color = choice(colors1)
            balls[k].vx = rnd(0, 80) / 20
            balls[k].vy = rnd(0, 80) / 20
        balls[k].draw_ball()
        label['text'] = str(score)


def move_all_balls():
    for i in range(len(balls)):
        if type(balls[i]) == Ball2:
            balls[i].move_ball2()
        else:
            balls[i].move_ball1()
        for j in range(len(balls)):
            dist = ((balls[i].x - balls[j].x)**2 +
                    (balls[i].y - balls[j].y)**2)**0.5
            if i != j and dist < (balls[i].r + balls[j].r):
                balls[i].collision(balls[j])
    root.after(delta_t, move_all_balls)


def writeinfile():
    global score, name
    scores = []
    with open('table.txt', 'r') as f:
        for i in f:
            scores.append(i.split(',  '))
        scores.append([name, str(score) + '\n'])
        scores.sort(key=lambda s: int(s[1][0:len(s[1]) - 1]), reverse=True)
    with open('table.txt', 'w') as f:
        for i in scores:
            f.write(',  '.join(i))


balls = []
print('What\'s your name?')
name = input()
label = tk.Label(root, bg='white', fg='black', width=20)
label.pack()
for i in range(balls_number1):
    b = Ball1(rnd(7, 15), choice(colors1))
    balls.append(b)
for i in range(balls_number2):
    b = Ball2(rnd(20, 50), choice(colors2))
    balls.append(b)
move_all_balls()
canv.bind('<Button-1>', click)

tk.mainloop()

try:
    writeinfile()
except FileNotFoundError:
    with open('table.txt', 'w') as f:
        f.write(name + ',  ' + str(score) + '\n')
