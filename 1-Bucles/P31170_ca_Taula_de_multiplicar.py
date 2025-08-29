# Taula de multiplicar
# https://jutge.org/problems/P31170_ca
# P31170_ca:std:none:
# Created on 8/29/2025, 2:09:52 AM by 徐渭

from yogi import read

n = read(int)

for i in range(1, 11):
    print(n, '*', i, ' = ', n*i, sep='')