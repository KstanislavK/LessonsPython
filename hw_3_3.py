def my_func(num_1, num_2, num_3):
    num_list = [num_1, num_2, num_3]
    max_num_1 = max(num_list)    
    x = num_list.index(max_num_1)
    del num_list[x]
    max_num_2 = max(num_list)
    return max_num_1 + max_num_2

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

print(f'Сумма наибольших двух чисел: {my_func(num_1, num_2, num_3)}')