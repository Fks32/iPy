from yogi import read
a1 = read(int)
b1 = read(int)
a2 = read(int)
b2 = read(int)

a = max(a1, a2)
b = min(b1, b2)
if a <= b:
    print(f'[{a},{b}]')
else:
    print('[]')