"""
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому
    классу атрибут instances, содержащий список всех созданных экземпляров этого класса.

Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке,
              в котором они были созданы.
"""
from functools import wraps


def track_instances(cls):
    cls.instances = []
    old_init = cls.__init__

    @wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self.instances.append(self)

    cls.__init__ = new_init
    return cls


# INPUT DATA:

print("\n# TEST_1:")


@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


obj1 = Person('object 1')
obj2 = Person('object 2')

print(Person.instances)

print("\n# TEST_2:")


@track_instances
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'Cat({self.name!r}, {self.breed!r})'


for _ in range(10):
    cat = Cat('Кемаль', 'Британский')

print(len(Cat.instances))

print("\n# TEST_3:")


@track_instances
class Gun:
    def __repr__(self):
        return 'Gun()'


for _ in range(10000):
    cat = Gun()

print(len(Gun.instances))
print(Gun.instances[3245])
