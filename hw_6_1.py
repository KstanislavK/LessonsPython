from itertools import cycle
from time import sleep
class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
    def running(self):
        color_dict = {self.__color[0]:7,self.__color[1]:2,self.__color[2]:10}
        for i in cycle(color_dict):
            print(i)
            sleep(color_dict[i])

a = TrafficLight()
a.running()