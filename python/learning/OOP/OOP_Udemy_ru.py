# === УРОК 40. МЕТОДЫ. ДЗ ===


class BankAccount:
    def __init__(self, clientID, clientFirstName, clientLastName):
        self.clientID = clientID
        self.clientFirstName = clientFirstName
        self.clientLastName = clientLastName
        self.balance = 0.0

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


agent = BankAccount('007', 'Me', 'Ow')
agent.add(500)
agent.withdraw(250)
print(agent.balance)

# === УРОК 41. МЕТОДЫ КЛАССА + ДЗ ===


class Gamers:
    # Начало поля класса
    activeGamers = 0  # Аттрибут уровня класса

    @classmethod  # Декоратор. Используется при создании метода класса
    def getActiveGamers(cls):  # cls т. к это метод уровня класса
        return Gamers.activeGamers

    @classmethod
    def gamerFromString(cls, dataString):
        nickname, age, level, points = dataString.split(', ')
        return cls(nickname, age, level, points)

    # Конец поля класса
    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamers.activeGamers += 1

    def getNickname(self):  # Геттер -
        return self.nickname

    def getAge(self):  # Это функция
        return self.age

    def getLevel(self):  # Возвращающая
        return self.getLevel

    def getPoints(self):  # Определенное значение
        return self.getPoints

    def isAdult(self):
        return self.age >= 18

    def getAdultLevelPermission(self):
        if self.isAdult:
            print('You can go to adult level')
        else:
            print('You can`t go to adult level')

    def logout(self):
        Gamers.activeGamers -= 1


# == Работа с аттрибутами метода класса ==
print(Gamers.activeGamers)
gamer1 = Gamers('dotaPro', 9, 100, 8)
print(Gamers.activeGamers)  # При создании объекта activeGamers += 1
gamer2 = Gamers('Hellboy', 24, 24, 50)
# setattr(gamer1, 'age', 99999)
print(gamer1.getAge())
gamer1.getAdultLevelPermission()
print(gamer2.getAge())
gamer2.getAdultLevelPermission()
print(Gamers.activeGamers)
gamer2.logout()
print(Gamers.activeGamers)
print(Gamers.getActiveGamers())

# == Работа с методами класса ==
james = Gamers.gamerFromString('James, 25, 4, 21')
jane = Gamers.gamerFromString('Jane, 225, 34, 211')
print(james.nickname)
print(jane.getAge())
print(Gamers.getActiveGamers())

myDict = dict.fromkeys((1, 2, 3), (('apple', 1), 'orange', 'banana'))  # Встроенный метод класса для работы со словарём

print(myDict)


# === УРОК 42. INHERITANCE. НАСЛЕДОВАНИЕ ===


class Car:
    wheelsNumber = 4

    def __init__(self, name, year, color, isCrushed):
        self.name = name
        self.year = year
        self.color = color
        self.isCrushed = isCrushed
        print('Car is created')

    def drive(self, city):
        print(self.name + ' drives to ' + city)

    def changeColor(self, newColor):
        self.color = newColor


class Truck(Car):  # Inheritance от Car
    wheelsNumber = 6  # Переопределение аттрибута предка под этот класс

    def __init__(self, name, year, color, isCrushed):  # Иницилизация класса
        Car.__init__(self, name, year, color, isCrushed)  # Иницилизация класса предка (Car)
        print('Truck is created')

    def drive(self, city):
        print('Truck' + self.name + ' drives to ' + city)

    def loadCargo(self, weight):
        print('The cargo is loaded. Weight is ' + str(weight) + 'kg')


manTruck = Truck('Man', 2015, 'white', False)
manTruck.drive('Kyiv')  # Изменение метода предка на новый метод
manTruck.loadCargo(2000) # Метод существующий только у наследника


# === УРОК 42. POLYMORPHISM. ПОЛИМОРФИЗМ ===


class Animal:  # Абстрактный класс предок всех последующих классов.
    def __init__(self, name):
        self.name = name

    def speak(self):
        # Ошибка "Не имплементировано". Предупреждает о том, что не имплементировали метод в классе потомке
        raise NotImplementedError(
            'Class successor must implement this method')  # "Класс наследник должен имплементировать этот метод"


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying meow')


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying pepe')


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying ????')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')

petList = [spike, tom, jerry]  # Сохраняется при вызове метод класса объекта


for pet in petList:
    pet.speak()

def petVoice(pet):  # Сохраняется при вызове метод класса объекта
    pet.speak()


petVoice(spike)
petVoice(tom)
petVoice(jerry)

freddy = Fish('Freddy')
petVoice(freddy)

# = ДЗ =


class GameCharacter():
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')

    def kill(self, name):
        name.health = 0
        print('Bang-bang, now you`re dead')


rasta = GameCharacter('Rasta', 82, 3)
rasta.speak()
warrior = Villain('Adolf', 100, 100)
warrior.speak()
print(rasta.health, warrior.health)
warrior.kill(rasta)
print(rasta.health, warrior.health)

# === УРОК 43. МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ ===


class Swimmable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swim')

    def swim(self):
        print('I`m swimming')


class Walkable:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')

    def walk(self):
        print('I`m walking')


class Flyable:
    def __init__(self, name):
        self.prototype = 444
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can fly')

    def fly(self):
        print('I`m flying')


class GameCharacter(Swimmable, Walkable, Flyable):  # Множественное наследование пишем через запятую
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    def greeting(self):
        print(f'Hello! My name is {self.name}')


james = GameCharacter('James')
james.greeting()
james.swim()
james.walk()
exm = james.fly()
print(exm)
print(james.prototype)
print(isinstance(james, Walkable))
print(isinstance(james, Swimmable))
print(isinstance(james, Flyable))
print(isinstance(james, dict))
print(isinstance(james, object))

print(isinstance(5, object))  # Всё в Python является частью class object, поэтому True
print(isinstance('a2-', object))
print(isinstance(['x', 0], object))

# === УРОК 44. MRO: Method Resolution Order ===

#     A
#   /  \
#  B   C
#  \  /
#   D


class A:
    def someMethod(self):
        print('Method of class A')


class B(A):
    def someMethod(self):
        print('Method of class B')


class C(A):
    def someMethod(self):
        print('Method of class C')


class D(B, C):
    def someMethod(self):
        print('Method of class D')


# __mro__, mro(), help()  - увидеть древо наследия
print(D.__mro__)
print(D.mro())
help(D)

someObject = D()
someObject.someMethod()


# === УРОК 45. Special Magic Methods __method_name__ ===


class Person(object):
    """Магия позволяет редактировать опции встроенных функций Python для используемого класса"""

    def __init__(self, name, lastName, age):
        self.name = name
        self.lastName = lastName
        self.age = age

    def __str__(self):
        print('def __str__(self):')
        return self.name + ' ' + self.lastName

    def __len__(self):
        return self.age

    def __del__(
            self):  # del называется "деструктором" объекта. Вызывается всегда, когда объект удаляет из памяти.
        # Сборщик замечает объект на который нет ссылок в памяти и удаляет его
        print('Person object with name ' + self.name + ' was deleted from memory')
        print(self)

    def __add__(self, other):
        return self.age + other.age

    def __and__(self, other):
        pass


jack = Person('Jack', 'White', 45)
jane = Person('Jane', 'Air', 23)

print(len([1, 2, 3, 4, 5]))
print(jack)
print(len(jack))
del jack

x = 25
y = 5
a = '6'
b = '3'
# print(x.__add__(y))
# print(a.__add__(b))
print('add ', jack.__add__(jane))
print(x.__and__(y))


# = ДЗ =


class Chain:
    def __init__(self, numberOfItems):
        self.numberOfItems = numberOfItems

    def __str__(self):
        return f'Chain with {self.numberOfItems} items'  # Изменяю вывод print(first)

    def __len__(self):  # print(len(first))
        return self.numberOfItems


homework = Chain(3)
print(homework)
print(len(homework))


class EmployeeNew:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        print(inst)
        return inst

    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Satya'


exampleNew = EmployeeNew()
print(exampleNew.name)


class EmployeeStr:
    def __init__(self):
        self.name = 'Swati'
        self.salary = 10000

    def __str__(self):
        return 'name=' + self.name + ' salary=$' + str(self.salary)


exampleStr = EmployeeStr()
print(exampleStr.name)
print(type(exampleStr))
print(type(len(1)))

# === СТРУКТУРА INHERITANCE ===


class Parent:  # объявляем родительский класс
    parent_attr = 100

    def __init__(self):
        print('Вызов родительского конструктора')

    def parent_method(self):
        print('Вызов родительского метода')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print('Атрибут родителя: {}'.format(Parent.parent_attr))


class Child(Parent):  # объявляем класс наследник
    def __init__(self):
        print('Вызов конструктора класса наследника')

    def child_method(self):
        print('Вызов метода класса наследника')


c = Child()  # экземпляр класса Child
c.child_method()  # вызов метода child_method
c.parent_method()  # вызов родительского метода parent_method
c.set_attr(200)  # еще раз вызов родительского метода
c.get_attr()  # снова вызов родительского метода


class NameOfClass:  # 1. class + название в котором все слова с большой буквы + ():

    def __init__(self, param1,
                 param2):  # 2. def + __init__ метод определяющий класс + (self) ключевое слово + (parameters)
        self.param1 = param1  # 3. self обращается к вновь созданному объекту и присваивает его аттрибуту значение
        self.param2 = param2  # self присваивает созданному объекту конкретное значение и отличное от других объектов


objectName1 = NameOfClass(param1='x', param2='y')  # Создание объекта и инициализация его аттрибутов
print(objectName1.param1, objectName1.param2)  # output: x, y
objectName2 = NameOfClass('x', 'y')
print(objectName2.param1, objectName2.param2, objectName2.someParameter)  # output: x, y, z
