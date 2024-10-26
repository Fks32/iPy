from yogi import read

# lectura de les dades d'entrada
num1 = read(int)
num2 = read(int)

if num2 > num1:
    num1 = num2

print(num1)