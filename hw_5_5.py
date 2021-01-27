with open(r'for_hw_5_5.txt', 'w+') as obj:
    line = input('Insert digits: ')
    obj.write(line)
    digits = line.split()
    total = 0
    for n in digits:
        total += int(n)
    obj.write(f'\nTotal summ = {total}')
    print(total)