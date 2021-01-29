class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        total_income = int(self._income['wage']) + int(self._income['bonus'])
        return total_income

name = input('Inser worker\'s name: ')
surname = input('Insert worker\'s surname: ')
position = input('Insert worker\'s position: ')
wage = input('Insert workers\'s wage: ')
bonus = input('Insert worker\'s bonus: ')
income = {'wage':wage, 'bonus':bonus}
worker = Position(name, surname, position, income)
print(f'Worker\'s full name: {worker.get_full_name()}')
print(f'{worker.get_full_name()} has total income: {worker.get_total_income()}')