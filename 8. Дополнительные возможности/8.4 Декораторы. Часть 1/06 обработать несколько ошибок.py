"""
Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных
    аргументов — типов исключений, и выводит текст:

    Исключение <тип исключения> обработано

если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
    Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
              также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import wraps


class IgnoreException:
    def __init__(self, *args):
        self.errors = args

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if isinstance(err, self.errors):
                    print(f"Исключение {type(err).__name__} обработано")
                else:
                    raise err
        return wrapper


# INPUT DATA:

print("\n# TEST_1:")


@IgnoreException(ZeroDivisionError, TypeError, ValueError)
def func_(x):
    return 1 / x


func_(0)

print("\n# TEST_2:")
min = IgnoreException(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))

print("\n# TEST_3:")


@IgnoreException()
def func_():
    raise ValueError


try:
    func_()
except Exception as error:
    print(type(error))

print("\n# TEST_4:")


@IgnoreException(TypeError)
def func_():
    raise ValueError


try:
    func_()
except Exception as error:
    print(type(error))

print("\n# TEST_5:")


@IgnoreException(ValueError, TypeError, NameError)
def func_():
    raise NameError


try:
    func_()
except Exception as error:
    print(type(error))

print("\n# TEST_6:")


@IgnoreException(ValueError, TypeError, ZeroDivisionError, NameError)
def func_():
    raise ZeroDivisionError


try:
    func_()
except Exception as error:
    print(type(error))

print("\n# TEST_7:")


@IgnoreException(ValueError, NameError, ZeroDivisionError, TypeError)
def func_(a, b, c):
    raise NameError


try:
    func_(1, 2, c=10)
except Exception as error:
    print(type(error))

print("\n# TEST_8:")


@IgnoreException(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    """beegeek"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())
