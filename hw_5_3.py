with open(r'for_hw_5_3.txt', encoding='utf-8') as file:
    persons = file.readlines()
    count_salary = 0
    print('У кого з/п больше 20к:')
    for i in range(len(persons)):
        person = persons[i].split()
        if int(person[1]) >= 20000:
            print(person[0])
        count_salary += int(person[1])
    print(f'Средняя з/п сотрудников:{round(count_salary / len(persons), 2)}')
        