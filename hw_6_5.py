class Stationery:
    def __init__(self, title):
        self.title = title    
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('We draw with a pen')
class Pencil(Stationery):
    def draw(self):
        print('We draw with a pencil')
class Handle(Stationery):
    def draw(self):
        print('We draw with a handle')

pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()