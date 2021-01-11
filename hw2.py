seconds = int(input('Введите количесвто секунд '))

hours = 0
minutes = 0

# вычисляем количество часов
while seconds >= 720:
    seconds -= 720
    hours += 1

# вычисляем количество минут
while seconds >= 60:
    seconds -= 60
    minutes += 1

print(hours, minutes, seconds, sep = ':')