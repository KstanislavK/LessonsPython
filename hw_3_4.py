def my_func_1(x, y):
    """с помощью ** """
    return 1 / x**(abs(y))

def my_func_2(x, y):
    """с помощью цикла"""
    z = 1
    for _ in range(abs(y)):
        z *= x
    return 1 / z

x = int(input('Введите число: '))
y = int(input('Введите отрицательную степень: '))

print(f'с помощью ** : {my_func_1(x, y)}')
print(f'с помощью цикла : {my_func_2(x, y)}')