from yogi import read
year = read(int)
leap = False
if year%100 == 0:
    leap = (year//100)%4 == 0
else:
    leap = year%4 == 0

if leap:
    print("YES")
else:
    print("NO")