def person(name, surname, year, city, email, tel_number):
    print (name, surname, year, city, email, tel_number)

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = input('Введите год вашего рождения: ')
city = input('Введите город проживания: ')
email = input('Введите ваш email: ')
tel_number = input('Введите номер телфона: ')

person(name=name, surname=surname, year=year, city=city, email=email, tel_number=tel_number)