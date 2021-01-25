from math import factorial

n = int(input('Введите число: '))

def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

for el in fact(n):
    print(el)