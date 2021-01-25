from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

с = 0
my_list = [1, 2, 3, 4, 5, 6]
for el in cycle(my_list):
    if с > 15:
        break
    print(el)
    с += 1