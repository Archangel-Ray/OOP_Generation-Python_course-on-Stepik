"""
Реализуйте функцию anything(), которая возвращает такой объект,
результат сравнения с которым c помощью операторов ==, !=, >, <, >= и <= всегда равен True.
"""
import math
import re


class AlwaysTrue:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __gt__ = __le__ = __ge__ = __eq__


def anything():
    return AlwaysTrue()


# INPUT DATA:

print("\n# TEST_1:")
print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)

print("\n# TEST_2:")
print(anything() != set())
print(anything() < {})
print(anything() > ())
print(anything() >= True)
print(anything() <= False)
print(anything() == id)

print("\n# TEST_3:")
print(anything() != (1, 2, 3))
print(anything() < {4, 5, 6})
print(anything() > range(180))
print(anything() >= {1: 'one'})
print(anything() <= ['', [], (), set])
print(anything() == any)
print(anything() != any)
print(anything() > any)
print(anything() < all)
print(anything() <= all)
print(anything() >= all)

print("\n# TEST_4:")
print(anything() == filter)
print(anything() != filter)
print(anything() < filter)
print(anything() > filter)
print(anything() >= filter)
print(anything() <= filter)
print(anything() == anything())
print(anything() != anything())
print(anything() < anything())
print(anything() > anything())
print(anything() >= anything())
print(anything() <= anything())
