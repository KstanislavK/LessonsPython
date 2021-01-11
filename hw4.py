num = int(input('Введите целое положительное число: '))

max_number = 0

while num != 0:
    last_num = num % 10
    if last_num > max_number:
        max_number = last_num
    num = num // 10

print('Максимальная цифра:', max_number)