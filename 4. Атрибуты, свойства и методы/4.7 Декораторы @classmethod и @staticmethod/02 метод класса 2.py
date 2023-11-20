"""
Реализуйте класс Rectangle, описывающий прямоугольник.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    length — длина прямоугольника
    width — ширина прямоугольника

Экземпляр класса Rectangle должен иметь два атрибута:

    length — длина прямоугольника
    width — ширина прямоугольника

Класс Rectangle должен иметь один метод класса:

    square() — метод, принимающий в качестве аргумента число side и возвращающий экземпляр класса Rectangle
                c длиной и шириной, равными side

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Rectangle:
    def __init__(self, length_, width_):
        self.length = length_
        self.width = width_

    @classmethod
    def square(cls, side_):
        return Rectangle(side_, side_)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)

# TEST_2:
print('\nтест 2')
rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)

# TEST_3:
print('\nтест 3')
array = [416, 347, 228, 276, 159, 54, 302, 256, 355, 57, 370, 309, 455, 242, 345, 90, 413, 77, 143, 494, 397, 380,
         477, 391, 139, 421, 367, 275, 397, 181]

for side in array:
    rectangle = Rectangle.square(side)
    print(rectangle.length == rectangle.width)

# TEST_4:
print('\nтест 4')
array = [(99, 297), (215, 472), (270, 80), (453, 215), (333, 360), (52, 426),
         (307, 257), (425, 493), (291, 437), (57, 415)]


for length, width in array:
    rectangle = Rectangle(length, width)
    print(f'Длина = {rectangle.length}, Ширина = {rectangle.width}')

# TEST_5:
print('\nтест 5')
rectangle = Rectangle(1, 2)
print(hasattr(rectangle, 'length'))
print(hasattr(rectangle, 'width'))
