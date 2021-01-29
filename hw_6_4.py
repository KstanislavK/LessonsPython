class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'The {self.name} starts movement'
    def stop(self):
        return f'The {self.name} stops'
    def turn(self, direction):
        return f'The {self.name} turns {direction}'
    def show_speed(self):
        return f'The {self.name} goes with speed {self.speed}'
    def police(self):
        if self.is_police == True:
            return 'It is a police car'
        else:
            return 'It is not a police car'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'OVERSPEED!!!'
        else:
            return f'The {self.name} is going with speed {self.speed}'
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'OVERSPEED!!!'
        else:
            return f'The {self.name} is going with speed {self.speed}'
class PoliceCar(Car):
    pass
town_car = TownCar(80, 'blue', 'CrownVictoria', False)
sport_car = SportCar(200, 'red', 'Ferrari', False)
work_car = WorkCar(20, 'gray', 'MAN', False)
police_car = PoliceCar(150, 'black&white', 'Interceptor', True)
print(town_car.show_speed())
print(town_car.turn('left'))
print(town_car.police())
print(sport_car.go())
print(sport_car.show_speed())
print(sport_car.name)
print(work_car.color)
print(work_car.show_speed())
print(police_car.police())
print(police_car.color)