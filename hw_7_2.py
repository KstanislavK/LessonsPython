from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def length(self):
        pass

class Coat(Clothes):
    @property
    def length(self):
        x = round(int(self.size) / 6.5 + 0.5, 2)
        return x
class Suit(Clothes):
    @property
    def length(self):
        x = round(int(self.size) * 2 + 0.3, 2)
        return x   

name = input('What type of clothes? (coat/suit): ').lower()
size = input('Insert size: ')
if name == 'coat':
    print(f'For new {name} you need {Coat(size).length} of textile')
elif name == 'suit':
    print(f'For new {name} you need {Suit(size).length} of textile')