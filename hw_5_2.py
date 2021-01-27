with open(r'test.txt') as file:
    line_list = file.readlines()
    print(f'Количество строк: {len(line_list)}')
    for i in range(len(line_list)):
        print(f'Количество слов в строке {i+1} - {len(line_list[i].split())}')