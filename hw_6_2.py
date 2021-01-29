class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass(self, mass_1=25, thickness=5):
        x = int(self._length) * int(self._width) * int(mass_1) * int(thickness)
        return x

length = input('Inser length of the road: ')
width = input('Inser width of the road: ')
# mass_1 = input('Insert mass for 1 sm: ')
# thickness = input('Insert thickness of the road: ')
a = Road(length, width)
print(a.mass())
#print(a.mass(mass_1=mass_1, thickness=thickness))