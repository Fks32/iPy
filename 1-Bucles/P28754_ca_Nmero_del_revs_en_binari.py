# Número del revés en binari
# https://jutge.org/problems/P28754_ca
# P28754_ca:std:none:
# Created on 8/29/2025, 3:32:21 PM by 徐渭

from yogi import read

n = read(int)

rev = ''
while n > 1:
    rev += f'{n%2}'
    n //= 2
rev += f'{n}'
print(rev)