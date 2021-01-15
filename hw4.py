phrase = input('Введите строку \n')
phrase_list = phrase.split()
for i, val in enumerate(phrase_list, start = 1):
    print(i, val[:10])