"""
Реализуйте класс Rectangle, описывающий прямоугольник.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    length — длина прямоугольника
    width — ширина прямоугольника

Экземпляр класса Rectangle должен иметь два атрибута:

    length — длина прямоугольника
    width — ширина прямоугольника

Класс Rectangle должен иметь два свойства:

    perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
    area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Rectangle:
    def __init__(self, length_, width_):
        self.length = length_
        self.width = width_

    def get_perimeter(self):
        return (self.length + self.width) * 2

    perimeter = property(get_perimeter)

    def get_area(self):
        return self.length * self.width

    area = property(get_area)


# INPUT DATA:

# TEST_1:
rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

# TEST_2:
rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

# TEST_3:
rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')
