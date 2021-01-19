def division(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return 'Второе число не может быть равно 0'

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
print(division(a, b))
