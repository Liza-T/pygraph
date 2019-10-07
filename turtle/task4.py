import turtle as t

t.shape('turtle')
for i in range (1, 11):
    for j in range(4):
        t.forward(i*20)
        t.left(90)
    t.penup()
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.pendown()
