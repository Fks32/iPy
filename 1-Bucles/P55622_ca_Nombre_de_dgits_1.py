# Nombre de dígits (1)
# https://jutge.org/problems/P55622_ca
# P55622_ca:std:none:
# Created on 8/29/2025, 2:14:11 AM by 徐渭

from yogi import read

n = read(int)
num = n
d = 1
while (num > 9):
    d += 1
    num //= 10

print('El nombre de digits de', n, 'es', d, end='.\n')
    