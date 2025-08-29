# Màxim comú divisor
# https://jutge.org/problems/P67723_ca
# P67723_ca:std:none:
# Created on 8/29/2025, 3:36:22 PM by 徐渭

from yogi import read

a = read(int)
b = read(int)
x = a
y = b

if a < b:
    a,b = b,a

while b != 0:
    r = a % b
    a = b
    b = r

print('El mcd de', x, 'i', y, 'es', a, end='.\n')