"""
1. Реализуйте функцию is_iterable(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:

    obj — произвольный объект

Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""
from collections.abc import Iterable, Iterator


def is_iterable(obj):
    return isinstance(obj, Iterable)


def is_iterator(obj):
    return isinstance(obj, Iterator)


print('\n# INPUT DATA:')

print('\n# TEST_1:')
print(is_iterable(123))
print(is_iterable([1, 2, 3]))
print(is_iterable((1, 2, 3)))
print(is_iterable('123'))
print(is_iterable(iter('123')))
print(is_iterable(map(int, '123')))

print('\n# TEST_2:')
print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))
