import turtle as t

n=12

t.shape('turtle')
for i in range (n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360/n)
