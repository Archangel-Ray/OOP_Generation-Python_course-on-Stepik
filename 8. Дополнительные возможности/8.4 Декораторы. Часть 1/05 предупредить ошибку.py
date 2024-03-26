"""
Реализуйте класс декоратор @exception_decorator, который возвращает

    кортеж (value, None), если декорируемая функция завершила свою работу без возбуждения исключения,
                          где value — возвращаемое значение декорируемой функции
    кортеж (None, errortype), если во время выполнения декорируемой функции было возбуждено исключение,
                              где errortype — тип возбужденного исключения

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
              также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import update_wrapper


class ExceptionDecorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as err:
            return None, type(err)


# INPUT DATA:

print("\n# TEST_1:")


@ExceptionDecorator
def func_(x):
    return 2 * x + 1


print(func_(1))
print(func_('bee'))

print("\n# TEST_2:")


@ExceptionDecorator
def f(x, y):
    return x * y


print(f('stepik', 10))

print("\n# TEST_3:")


@ExceptionDecorator
def f(x, y):
    return x * y


print(f('stepik', 'stepik'))

print("\n# TEST_4:")


@ExceptionDecorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f(1, 2, 3, param1=4, param2=10))

print("\n# TEST_5:")


@ExceptionDecorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2='10'))

print("\n# TEST_6:")
sum = ExceptionDecorator(sum)

print(sum(['199', '1', 187]))
