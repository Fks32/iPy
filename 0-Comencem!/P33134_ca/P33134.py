import turtle as t
from yogi import read

com = read(str)
num = read(int)

if com == "cercle":
    t.circle(num)
elif com == "quadrat":
    for i in range (4):
        t.forward(num)
        t.left(90)
elif com == "rectangle":
    num2 = read(int)
    t.forward(num)
    t.left(90)
    t.forward(num2)
    t.left(90)
    t.forward(num)
    t.left(90)
    t.forward(num2)

t.done()