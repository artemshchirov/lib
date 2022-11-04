from collections import namedtuple

jake = ('Jake', 'Smith', 19, 'male')
jim = ('Jim', 'Blade', 23, 'male')

# jane = ('Jane', 'Morison', 20, 'female')
Person = namedtuple("Person", "name surname age gender")
jane = Person(name='Jane', surname='Morison', age=20, gender='female')

print(jane.name)
print(jane.age)
print(jane)
jane = jane._replace(surname="Blade")
print(jane)

