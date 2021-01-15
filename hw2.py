x = input('Введите элементы через запятую \n')
elements = x.split(',')

for i in range(0, len(elements)-1, 2):
        elements[i+1], elements[i] = elements[i], elements[i+1]

print(elements)