from yogi import read
a1 = read(int)
b1 = read(int)
a2 = read(int)
b2 = read(int)

a = max(a1, a2)
b = max(b1, b2)

if a1 == a2 and b1 == b2:
    print(f'=')
elif a1 == a and b2 == b:
    print('1')
elif a2 == a and b1 == b:
    print('2')
else:
    print('?')