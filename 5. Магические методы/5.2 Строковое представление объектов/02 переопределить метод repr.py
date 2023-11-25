"""
Вам доступен класс Rectangle, описывающий прямоугольник.
При создании экземпляра класс принимает два аргумента в следующем порядке:

    length — длина прямоугольника
    width — ширина прямоугольника

Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:

Rectangle(<длина прямоугольника>, <ширина прямоугольника>)

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Rectangle нет, она может быть произвольной.
"""


class Rectangle:
    def __init__(self, length_, width_):
        self.length = length_
        self.width = width_

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


# INPUT DATA:

# TEST_1:
print("\nтест 1")
rectangle = Rectangle(1, 2)

print(str(rectangle))
print(repr(rectangle))

# TEST_2:
print("\nтест 2")
rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)

print(rectangle1)
print(repr(rectangle2))

# TEST_3:
print("\nтест 3")
figures = [Rectangle(1, 2), Rectangle(3, 4)]

print(figures)

# TEST_4:
print("\nтест 4")
array = [(80, 56), (77, 22), (28, 78), (33, 75), (47, 30), (79, 60), (47, 69), (26, 27), (39, 48), (64, 36)]
for length, width in array:
    rectangle = Rectangle(length, width)
    print(rectangle, repr(rectangle), sep='\n', end='\n\n')
