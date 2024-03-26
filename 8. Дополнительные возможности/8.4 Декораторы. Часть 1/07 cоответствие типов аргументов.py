"""
Реализуйте класс декоратор @type_check, который принимает один аргумент:

    types — список, элементами которого являются типы данных

Декоратор должен проверять, что типы всех позиционных аргументов, передаваемых в декорируемую функцию, полностью
    сопоставляются с типами из списка types, то есть типом первого аргумента является первый элемент списка types,
    типом второго аргумента — второй элемент списка types, и так далее. Если данное условие не выполняется, должно
    быть возбуждено исключение TypeError.

Если количество позиционных аргументов больше, чем количество элементов в списке types, то не сопоставляемые аргументы
    не должны учитываться при проверке. Если количество позиционных аргументов меньше чем количество элементов в списке
    types, то не сопоставляемые типы из списка types не должны учитываться при проверке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
              также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import wraps


class TypeCheck:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg_in, arg_out in zip(self.types, args):
                if arg_in != type(arg_out):
                    raise TypeError
            for arg_in, arg_out in zip(self.types, kwargs.values()):
                if arg_in != type(arg_out):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper


# INPUT DATA:

print("\n# TEST_1:")


@TypeCheck([int, int])
def add(a, b):
    return a + b


print(add(1, 2))

print("\n# TEST_2:")


@TypeCheck([int, int])
def add(a, b):
    return a + b


try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))

print("\n# TEST_3:")


@TypeCheck([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(1, 2))

print("\n# TEST_4:")


@TypeCheck([int, int])
def add(a, b, c):
    return a + b + c


print(add(1, 2, 3.0))

print("\n# TEST_5:")


@TypeCheck([])
def add(a, b):
    return a + b


print(add(1, 2))

print("\n# TEST_6:")


@TypeCheck([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))
