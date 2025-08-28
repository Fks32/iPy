import yogi

a = yogi.read(int)
b = yogi.read(int)
c = yogi.read(int)

if a < b:
    a = b

if a < c:
    a = c

print(a)