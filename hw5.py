money = int(input('Укажите выручку '))
costs = int(input('Укажите издержки '))
profit = int(money - costs)

if money > costs:
    print('Вы работаете с прибылью')
    print('Коэффициент рентабельности:', round(profit/costs, 2))
    num_workers = int(input('Сколько работников в фирме? '))
    print('Прибыль фирмы на одного рабочего: ', int(profit/num_workers))
elif money < costs:
    print('Фирма работает в убыток')
elif money == costs:
    print('В фирме стагнация')

