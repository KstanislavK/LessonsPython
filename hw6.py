count_goods = int(input('Сколько товаров принимаем? '))
goods = {}
structure = []
total = []
for i in range(count_goods):    
    goods['название'] = input('Название: ')
    goods['цена'] = input('цена: ')
    goods['количество'] = input('количество: ')
    goods['единицы'] = input('единицы: ')
    structure.append(i+1)
    structure.append(goods)
    structure = tuple(structure)
    total.append(structure)
    goods = {}
    structure = []

analytic_dict = {}

for m in total:
    for key, val in m[1].items():
        if key not in analytic_dict:
            analytic_dict[key] = []
            analytic_dict[key].append(val)
        else:
            analytic_dict[key].append(val)

print(total)
print(analytic_dict)