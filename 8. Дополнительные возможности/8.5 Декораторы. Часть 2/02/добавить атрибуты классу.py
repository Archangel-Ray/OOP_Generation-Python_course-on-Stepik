"""
Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса,
    является объектом типа mappingproxy, а не dict.

class MyClass:
    pass


print(type(MyClass.__dict__))

выводит:

<class 'mappingproxy'>

Тип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством методов,
    а главное — отсутствием магического метода __setitem__(). Это значит, в объект типа mappingproxy нельзя
    напрямую добавить новую пару ключ-значение, а также изменить значение имеющегося ключа.

class MyClass:
    pass


MyClass.__dict__['__doc__'] = 'docstring'

приводит к возбуждению исключения:

TypeError: 'mappingproxy' object does not support item assignment

Для добавления классу необходимого атрибута можно использовать функцию setattr().

class MyClass:
    pass


setattr(MyClass, '__doc__', 'docstring')

print(MyClass.__doc__)

выводит:

docstring

Реализуйте декоратор @add_attr_to_class для декорирования класса. Декоратор должен принимать произвольное количество
    именованных аргументов и добавлять их декорируемому классу в качестве атрибутов.
"""


def add_attr_to_class(**kwargs):
    def decorator(cls):
        for name, value in kwargs.items():
            setattr(cls, name, value)
        return cls

    return decorator


# INPUT DATA:

print("\n# TEST_1:")


@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass


print(MyClass.first_attr)
print(MyClass.second_attr)

print("\n# TEST_2:")


@add_attr_to_class(name='Кемаль', breed='Британский')
class Cat:
    pass


print(Cat.name)
print(Cat.breed)

print("\n# TEST_3:")
data = {'name': 'John', 'surname': 'Doe'}


@add_attr_to_class(**data)
class Person:
    def __init__(self, name=None, surname=None):
        self.name = name or self.name
        self.surname = surname or self.surname


person = Person()
print(person.name)
print(person.surname)

print("\n# TEST_4:")


@add_attr_to_class(shoot1='pif', shoot2='paf')
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()
