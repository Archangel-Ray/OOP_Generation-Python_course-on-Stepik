"""
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:

    radius — радиус круга

Экземпляр класса Circle должен иметь один атрибут:

    radius — радиус круга

Класс Circle должен иметь один метод класса:

    from_diameter() — метод, принимающий в качестве аргумента диаметр круга и возвращающий экземпляр класса Circle,
                       созданный на основе переданного диаметра

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diam):
        return Circle(diam / 2)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
circle = Circle(5)

print(circle.radius)

# TEST_2:
print('\nтест 2')
circle = Circle.from_diameter(10)

print(circle.radius)

# TEST_3:
print('\nтест 3')
circle1 = Circle(51.5)
circle2 = Circle.from_diameter(45)

print(circle1.radius)
print(circle2.radius)

# TEST_4:
print('\nтест 4')
array = [473, 474, 75, 182, 51, 491, 493, 494, 347, 305, 290, 381, 170, 355, 326, 97, 183, 120, 216, 475, 66, 306, 193,
         257, 482, 200, 350, 236, 471, 468]

for diameter in array:
    circle = Circle.from_diameter(diameter)
    print(circle.radius)

# TEST_5:
print('\nтест 5')
circle = Circle.from_diameter(120)
print(hasattr(circle, 'radius'))
