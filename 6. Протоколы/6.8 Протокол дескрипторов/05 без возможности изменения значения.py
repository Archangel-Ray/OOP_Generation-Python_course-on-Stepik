"""
Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое
    число в заданном диапазоне. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    start — целое число
     — целое число
    cache — булево значение, по умолчанию равняется False

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно.
    Если в качестве значения параметра cache при создании дескриптора было указано значение True, при каждом
    обращении к атрибуту дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.

При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:

    Изменение невозможно

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется,
                что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RandomNumber нет, она может быть произвольной.
"""
from random import randint


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start, self.end = start, end
        self.first = randint(start, end)
        self.cache = cache

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj:
            return self.first if self.cache else randint(self.start, self.end)
        return self

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")


# INPUT DATA:

# TEST_1:
print("\nтест 1")


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])

# TEST_2:
print("\nтест 2")


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])

# TEST_3:
print("\nтест 3")


class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()
value_ = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value_)
print(magicpoint.x == value_)
print(magicpoint.x == value_)

# TEST_4:
print("\nтест 4")


class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)

# TEST_5:
print("\nтест 5")


class MagicPoint:
    x = RandomNumber(20, 100, True)


magicpoint = MagicPoint()

value_ = magicpoint.x

for _ in range(20):
    print(magicpoint.x == value_)

# TEST_6:
print("\nтест 6")


class MagicPoint:
    x = RandomNumber(-1000, 1000)


magicpoint = MagicPoint()

for _ in range(50):
    print(magicpoint.x in range(-1000, 1001))

# TEST_7:
print("\nтест 7")


class MagicPoint:
    x = RandomNumber(-1000, 1000)

    def __init__(self, x):
        self.x = x


try:
    magicpoint = MagicPoint(150)
except AttributeError as e:
    print(e)

# TEST_8:
print("\nтест 8")


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


print(MagicPoint.x.__class__)
print(MagicPoint.y.__class__)
print(MagicPoint.z.__class__)
