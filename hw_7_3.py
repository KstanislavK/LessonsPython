class Cell:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    def __sub__(self, other):
        if self.number - other.number > 0:
            return self.number - other.number
        else:
            return 'Вычитание не получится'
    def __mul__(self, other):
        return self.number * other.number
    def __truediv__(self, other):
        return self.number // other.number
    def make_order(self, number_in_row):
        cell_order = ''
        rows = self.number // number_in_row
        last_row = self.number % number_in_row
        for _ in range(rows):
            cell_order += str('\\n' + '*' * number_in_row)
        if last_row != 0:
            cell_order = cell_order + str('\\n' + '*' * last_row)
        return cell_order[2:]

cell_1 = Cell(40)
cell_2 = Cell(30)
print(cell_1 + cell_2) #сложение клеток, переопределение __add__
print(cell_1 - cell_2) #вычитание клеток, переопределение __sub__
print(cell_1 * cell_2) #умножение клеток, переопределение __mul__
print(cell_1 / cell_2) #деление клеток, переопределение __truediv__
print(Cell(27).make_order(5)) #вывод ячеек по рядам