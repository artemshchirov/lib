from abc import ABC, abstractmethod


class Movable(ABC):

    @abstractmethod
    def move(self):
        """Переместить объект"""

    @property
    @abstractmethod
    def speed(self):
        """Скорость объекта"""


class Car(Movable):

    speed = 10

    def __init__(self):
        self.x = 0
        self.color = 'red'

    def move(self):
        self.x += Car.speed

    def change_color(self, color: str):
        self.color = color


class Person(Movable):
    speed = 3

    def __init__(self):
        self.x = 0
        self.age = 25

    def move(self):
        self.x += self.speed

    def say(self, words: str):
        print(words)


print(issubclass(Car, Movable), isinstance(Car(), Movable))
print(issubclass(Person, Movable), isinstance(Person(), Movable))


Tesla = Car()
Tesla.move()
print(Tesla.speed)
print(Tesla.color)
Tesla.change_color('green')
print(Tesla.color)

Artem = Person()
Artem.move()
print(Artem.speed)
Artem.say('Hello, I am human!')


class Building:
    """Определение жилого дома
    
    :number: номер дома, целое число
    :entrance_x: подъезд номер x, 
        словарь содержащий в себе {номер квартиры:имя жильцов},
        имена - строка если житель один или семья. Список, если житель не один и не семья
    :house: дом - кортеж, который содержит подъезды с жителями
    """
    number = 33 

    entrance_1 = {
        1:"Джек, Анна",
        2:"Макс",
    }
    entrance_2 = {
        3:"Алекс",  
        4:["Мария", "Саша, Боб"],
        5:["Никита, Аня", "Оля, Павел"],
    }
    entrance_3 = {
        6:"Кристина, Олег, Максим",
        7:"Макс",
    }
    entrance_4 = {
        8:["Марина", "Артём"],
        9:"Адам, Ева",
    }

    house = (
        entrance_1, 
        entrance_2,
        entrance_3, 
        entrance_4,
    )

    def call(en, id):
        return Building.house[en].get(id)

dicty = {1:'a', 2:'b', 3:['c', 'd']}
print(dicty.clear())

def asd(num):
    print('ok', num)

print(asd)
cd = asd
print(cd)
cd(1)
