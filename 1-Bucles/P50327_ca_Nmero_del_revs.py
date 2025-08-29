# Número del revés
# https://jutge.org/problems/P50327_ca
# P50327_ca:std:none:
# Created on 8/29/2025, 3:24:55 PM by 徐渭

from yogi import read

n = read(int)

rev = ''
while n > 9:
    rev += f'{n%10}'
    n //= 10
rev += f'{n}'
print(rev)
