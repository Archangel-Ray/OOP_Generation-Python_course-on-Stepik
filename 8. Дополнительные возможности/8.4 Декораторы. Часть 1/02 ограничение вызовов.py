"""
Реализуйте класс декоратор @limited_calls, который принимает один аргумент:

    n — целое число

Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз,
    должно быть возбуждено исключение MaxCallsException с текстом:

    Превышено допустимое количество вызовов

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
              также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
from functools import wraps
import random


class MaxCallsException(Exception):
    pass


class LimitedCalls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.n:
                self.n -= 1
                return func(*args, **kwargs)
            raise MaxCallsException("Превышено допустимое количество вызовов")

        return wrapper


# INPUT DATA:

print("\n# TEST_1:")


@LimitedCalls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)

print("\n# TEST_2:")


@LimitedCalls(5)
def positive_sum(*args):
    return sum(args)


for _ in range(4):
    positive_sum(*(random.randint(1, 100) for _ in range(10)))

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

try:
    print(positive_sum(10, 124, 124, 786, 11))
except MaxCallsException as e:
    print(e)

print("\n# TEST_3:")


@LimitedCalls(5)
def concat(a, b, c):
    return a + b + c


for _ in range(5):
    print(concat('123', '456', '789'))

try:
    print(concat('123', '456', '789'))
except MaxCallsException as e:
    print(e)

print("\n# TEST_4:")


@LimitedCalls(10)
def power(a, n):
    return a ** n


for _ in range(10):
    power(2, 3)

try:
    print(power(2, 3))
except MaxCallsException as e:
    print(e)

print("\n# TEST_5:")


@LimitedCalls(10)
def power(a, n):
    """degree"""
    return a ** n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))
