"""
Вам доступен декоратор @reverse_args, который передает все позиционные аргументы в декорируемую функцию в обратном
    порядке. Реализуйте декоратор @reverse_args в виде класса декоратора.

Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также
                должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


class ReverseArgs:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)


# INPUT DATA:

print("\n# TEST_1:")


@ReverseArgs
def power(a, n):
    return a ** n


print(power(2, 3))

print("\n# TEST_2:")


@ReverseArgs
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))

print("\n# TEST_3:")


@ReverseArgs
def operation(a, b, c):
    return a // b + c


print(operation(10, 20, 80))

print("\n# TEST_4:")


@ReverseArgs
def operation(a, b):
    """integer division"""
    return a // b


print(operation.__name__)
print(operation.__doc__)
print(operation(90, 0))

print("\n# TEST_5:")


@ReverseArgs
def operation(a, b):
    return a // b


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

print("\n# TEST_6:")


@ReverseArgs
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))

print("\n# TEST_7:")


@ReverseArgs
def operation(a, b, value=10):
    return a // b + value


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')

print("\n# TEST_8:")


@ReverseArgs
def operation(a, b, value1=10, value2=30):
    return a // b - value1 + value2


print(operation(140, 70, value1=50, value2=100))

print("\n# TEST_9:")
print(ReverseArgs)
print(type(ReverseArgs))
