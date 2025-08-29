import turtle as t
from yogi import read

n = read(int)
m = read(int)
l = m
i = 0
while i < n:
    t.forward(l)
    t.left(90)
    t.forward(l)
    t.left(90)
    i += 1
    l += m
t.done()