my_list = [7, 5, 3, 3, 2]
n = ''
while n.lower() != 'q':
    print('Введите новый элемент. Для выхода введите "q"')
    n = input()
    if n.lower() == 'q':
        print('Всего доброго')
        break
    elif int(n) in my_list:
        x = len(my_list) - 1 - my_list[::-1].index(int(n))
        my_list.insert(x , int(n))
        print(my_list)
    else:
        my_list.append(int(n))
        my_list.sort(reverse=True)
    print(my_list)