month = int(input())
dict = {
    1 : 'зима',
    2 : 'зима',
    3 : 'весна',
    4 : 'весна',
    5 : 'весна',
    6 : 'лето',
    7 : 'лето',
    8 : 'лето',
    9 : 'осень',
    10 : 'осень',
    11 : 'осень',
    12 : 'зима'
}

print(dict[month])

seasons = ['зима', 'весна', 'лето', 'осень']
if 1 <= month <= 2 or month == 12:
    print(seasons[0])
elif 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[2])
else:
    print(seasons[3])