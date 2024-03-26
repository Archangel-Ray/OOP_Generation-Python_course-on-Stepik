"""
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
    принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть
    возбуждено исключение TypeError с текстом:

    Аргументы должны принадлежать типам int или float

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
              должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import update_wrapper


class TakesNumbers:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, (int, float)):
                raise TypeError("Аргументы должны принадлежать типам int или float")
        return self.func(*args, **kwargs)


# INPUT DATA:

print("\n# TEST_1:")


@TakesNumbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))

print("\n# TEST_2:")


@TakesNumbers
def mul(a, b):
    return a * b


try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)

print("\n# TEST_3:")


@TakesNumbers
def mul(a, b):
    return a * b


try:
    print(mul('1', 2))
except TypeError as error:
    print(error)

print("\n# TEST_4:")


@TakesNumbers
def mul(a, b):
    return a * b


try:
    print(mul('1', '2'))
except TypeError as error:
    print(error)

print("\n# TEST_5:")


@TakesNumbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b='2'))
except TypeError as error:
    print(error)

print("\n# TEST_6:")


@TakesNumbers
def mul(a, b=2):
    """multiplication"""
    return a * b


print(mul.__name__)
print(mul.__doc__)
print(mul(3, 4))

print("\n# TEST_7:")
print(TakesNumbers)

print("\n# TEST_8:")


@TakesNumbers
def mul(a, b=2):
    return a * b


print(mul(1, b=2))

print("\n# TEST_9:")


@TakesNumbers
def mul(a, b):
    return a * b


print(mul(a=1, b=2))
