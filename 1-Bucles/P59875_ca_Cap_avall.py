# Cap avall
# https://jutge.org/problems/P59875_ca
# P59875_ca:std:none:
# Created on 8/29/2025, 2:02:46 AM by 徐渭

from yogi import read

x = read(int)
y = read(int)

if x < y:
    x,y = y,x
i = x
while i >= y:
    print(i)
    i -= 1