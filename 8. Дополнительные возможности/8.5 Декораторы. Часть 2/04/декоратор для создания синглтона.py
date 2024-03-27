"""
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон,
то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.
"""
from functools import wraps


def singleton(cls):
    cls.instance = None
    cls_new = cls.__new__

    @wraps(cls_new)
    def new_new(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = cls_new(cls)
        return cls.instance

    cls.__new__ = new_new
    return cls


# INPUT DATA:

print("\n# TEST_1:")


@singleton
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)

print("\n# TEST_2:")


@singleton
class MyClass:
    pass


instances = [MyClass() for _ in range(100)]
obj = MyClass()
print(all(instance is obj for instance in instances))

print("\n# TEST_3:")


@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))
