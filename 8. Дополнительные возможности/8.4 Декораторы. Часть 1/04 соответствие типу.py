"""
Реализуйте класс декоратор @returns, который принимает один аргумент:

    datatype — тип данных

Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype.
    Если возвращаемое значение принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError.

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
              должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import wraps


class Returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, self.datatype):
                return value
            raise TypeError()
        return wrapper


# INPUT DATA:

print("\n# TEST_1:")


@Returns(int)
def add(a, b):
    return a + b


print(add(1, 2))

print("\n# TEST_2:")


@Returns(int)
def add(a, b):
    return a + b


try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))

print("\n# TEST_3:")


@Returns(list)
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))

print("\n# TEST_4:")


@Returns(list)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))

print("\n# TEST_5:")


@Returns(tuple)
def append_this(li, elem):
    """append_this docs"""
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2, 3], [4, 5, 6]))
except TypeError as e:
    print(type(e))

print("\n# TEST_6:")


@Returns(int)
def add(a, b):
    return a + b


print(add(a=10, b=5))
