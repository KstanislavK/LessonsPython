total = 0
line = ''

def sum_numbers(line, total):
    sum_num = 0
    for num in line:
        if num.lower() == 'q':
            break
        else:
            sum_num += int(num)
    return int(sum_num)
while 'q' not in line:    
    line = list(input('Введите числа через пробел, мы их будем суммировать, "q" - выход: ').split())
    total += sum_numbers(line, total)
    print(total)
else:
    print('Спасибо, что воспользовались нашим сервисом :-)')