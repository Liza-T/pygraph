import turtle as t

n = 100
t.shape('turtle')
t.speed(10)

def circle(m):
    for i in range (n):
        t.forward(4)
        if m == 0:
            t.left(3.6)
        else:
            t.right(3.6)

for i in range(6):
    circle(i%2)
    if i % 2 == 1:
        t.left(60)
