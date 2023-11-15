"""
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

    radius — радиус круга

Экземпляр класса Circle должен иметь три атрибута:

    _radius — радиус круга
    _diameter — диаметр круга
    _area — площадь круга

Класс Circle должен иметь три метода экземпляра:

    get_radius() — метод, возвращающий радиус круга
    get_diameter() — метод, возвращающий диаметр круга
    get_area() — метод, возвращающий площадь круга

Примечание 1. Площадь круга вычисляется по формуле πr2, где r — радиус круга, π — константа,
              которая выражает отношение длины окружности к ее диаметру.

Примечание 2. Импортировать константу ππ можно из модуля math:

from math import pi

Примечание 3. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""
from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * self.get_radius() ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


# INPUT DATA:

print('TEST 1:')
circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

# TEST_2:
print('TEST 2:')
circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

# TEST_3:
print('TEST 3:')
circle = Circle(50)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

# TEST_4:
print('TEST 4:')
circle = Circle(18.32)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

# TEST_5:
print('TEST 5:')
circle = Circle(0.7)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

# TEST_6:
print('TEST 6:')
circle = Circle(10)
print(hasattr(circle, '_radius'))
print(hasattr(circle, '_diameter'))
print(hasattr(circle, '_area'))
