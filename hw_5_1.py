with open(r'test.txt', 'a') as obj:
    line = 0
    while line != '':
        line = input('Insert data: ')
        obj.write(line + '\n')
