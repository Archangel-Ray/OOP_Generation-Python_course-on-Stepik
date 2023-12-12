"""
Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней.
При создании экземпляра класс должен принимать один аргумент:

    sides — количество граней игрального кубика

Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов.
При вызове он должен возвращать значение случайной грани игрального кубика.
Например, если кубик имеет 6 граней, экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6].

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Dice нет, она может быть произвольной.
"""
from random import randrange


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randrange(1, self.sides + 1)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])
print(kingdice())

# TEST_2:
print('\nтест 2')
kingdice = Dice(2)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])

# TEST_3:
print('\nтест 3')
kingdice = Dice(1)

print(kingdice() == 1)
print(kingdice() in [1, 2])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])

# TEST_4:
print('\nтест 4')
kingdice = Dice(100)

for _ in range(100):
    print(kingdice() in range(1, 101))

# TEST_5:
print('\nтест 5')
kingdice = Dice(20)
print(callable(kingdice))
