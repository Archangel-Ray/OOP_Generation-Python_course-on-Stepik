"""
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

    filename — имя json файла, содержимым которого является JSON объект

Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу
    каждую пару ключ-значение JSON объекта, содержащегося в этом файле.
"""
import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename) as file:
            for name, value in json.load(file).items():
                setattr(cls, name, value)
        return cls

    return decorator


# INPUT DATA:

print("\n# TEST_1:")
with open('test.json', 'w') as file_:
    file_.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)

print("\n# TEST_2:")
with open('test.json', 'w') as file_:
    file_.write('{"name": "John", "surname": "Doe"}')


@jsonattr('test.json')
class Person:
    pass


print(Person.name)
print(Person.surname)

print("\n# TEST_3:")
with open('test.json', 'w') as file_:
    file_.write('{"name": "Кемаль", "breed": "Британский"}')


@jsonattr('test.json')
class Cat:
    def __init__(self, name=None, breed=None):
        self.name = name or self.name
        self.surname = breed or self.breed


cat = Cat()
print(cat.name)
print(cat.breed)

print("\n# TEST_4:")
with open('test.json', 'w') as file_:
    file_.write('{"shoot1": "pif", "shoot2": "paf"}')


@jsonattr('test.json')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()
