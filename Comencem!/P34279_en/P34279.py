from yogi import read
h = read(int)
m = read(int)
s = read(int)
s += 1
if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
print(h//10, h%10, ':', m//10, m%10, ':', s//10, s%10, sep='')