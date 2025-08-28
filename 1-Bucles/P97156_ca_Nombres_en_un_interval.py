# Nombres en un interval
# https://jutge.org/problems/P97156
# P97156:std:none:
# Created on 8/29/2025, 1:29:13 AM by 徐渭

from yogi import read

a = read(int)
b = read(int)

for i in range(a, b):
    print(i,end=',')
if (a <= b):
    print(b)
else:
    print()