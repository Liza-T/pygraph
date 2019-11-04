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
            dist = ((self.x - other.x)**2 +
                    (self.y - other.y)**2)**0.5
            m1 = self.r
            m2 = other.r
            if abs(self.x - other.x)/dist >= 1:
                fi = 0
            elif (self.x - other.x > 0
                    and self.y - other.y > 0
                    or self.x - other.x < 0
                    and self.y - other.y < 0):
                fi = math.acos(abs(self.x - other.x) / dist)
            else:
                fi = math.pi - math.acos(abs(self.x - other.x)/dist)
            v01 = (self.vx ** 2 + self.vy ** 2) ** 0.5
            v02 = (other.vx ** 2 + other.vy ** 2) ** 0.5
            angle1 = math.acos(self.vx / v01)
            if self.vy < 0:
                angle1 = 2*math.pi - angle1
            angle2 = math.acos(other.vx / v02)
            if other.vy < 0:
                angle2 = 2*math.pi - angle2
            a1 = angle1 - fi
            a2 = angle2 - fi
            vx20 = v02 * math.cos(a2)
            vx10 = v01 * math.cos(a1)
            vx1 = 2 * vx20 * m2 / (m1 + m2) - vx10 * (m2 - m1) / (m2 + m1)
            vx2 = 2 * vx10 * m1 / (m1 + m2) - vx20 * (m2 - m1) / (m2 + m1)
            vy1 = v01 * math.sin(a1)
            vy2 = v02 * math.sin(a2)
            v1 = (vx1 ** 2 + vy1 ** 2) ** 0.5
            v2 = (vx2 ** 2 + vy2 ** 2) ** 0.5
            if vy1 != 0:
                a1 = math.acos(vx1 / v1) * vy1 / abs(vy1)
            else:
                a1 = math.acos(vx1 / v1)
            if vy2 != 0:
                a2 = math.acos(vx2 / v2) * vy2 / abs(vy2)
            else:
                a2 = math.acos(vx2 / v2)
            angle11 = (a1 + fi) % (math.pi * 2)
            angle22 = (a2 + fi) % (math.pi * 2)
            self.vx = v1 * math.cos(angle11)
            self.vy = v1 * math.sin(angle11)
            other.vx = v2 * math.cos(angle22)
            other.vy = v2 * math.sin(angle22)
            r = self.r + other.r - dist
            self.x += r * math.cos(fi)
            self.y += r * math.sin(fi)
            other.x -= r * math.cos(fi)
            other.y -= r * math.sin(fi)


class Ball1(Ball):

    def __init__(self, r, color):
        super().__init__(r, color)
        self.vx = rnd(0, 60)/20
        self.vy = rnd(0, 60)/20
        self.dt = 1

    def move_ball1(self):
        self.delete()
        a = 0.05
        self.x += self.vx * self.dt
        self.y += -(self.vy * self.dt - a * self.dt ** 2 / 2)
        self.vy -= a * self.dt
        self.reflection()
        self.draw_ball()


class Ball2(Ball):

    def __init__(self, r, color):
        super().__init__(r, color)
        self.vx = rnd(0, 40)/20
        self.vy = rnd(0, 40)/20

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
        if ((balls[i].x - event.x)**2 + 
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
            balls[k].vx = rnd(0, 40) / 20
            balls[k].vy = rnd(0, 40) / 20
        else:
            score += 10
            balls[k].r = rnd(7, 15)
            balls[k].color = choice(colors1)
            balls[k].vx = rnd(0, 60) / 20
            balls[k].vy = rnd(0, 60) / 20
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


def write():
    global score, name
    scores = []
    with open('table.txt', 'w') as f:
        pass
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

write()
