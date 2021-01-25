from sys import argv
hour, pay_hour, bonus = argv[1:]
def count_salary(hour, pay_hour, bonus):
    try:
        salary = float(hour) * float(pay_hour) + float(bonus)
        return salary
    except ValueError:
        return 'Invalid value'
print(count_salary(hour, pay_hour, bonus))
