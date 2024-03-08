"""
С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры
"""


class Shape:
    pass


class Polygon(Shape):
    pass


class Circle(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))

# TEST_2:
print("\nтест 2")
print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))

# TEST_3:
print("\nтест 3")
print(issubclass(Parallelogram, Quadrilateral))
print(issubclass(Rectangle, Quadrilateral))
print(issubclass(Square, Quadrilateral))

# TEST_4:
print("\nтест 4")
print(issubclass(IsoscelesTriangle, Quadrilateral))
print(issubclass(EquilateralTriangle, Quadrilateral))

print(issubclass(Parallelogram, Triangle))
print(issubclass(Rectangle, Triangle))
print(issubclass(Square, Triangle))

# TEST_5:
print("\nтест 5")
print(issubclass(IsoscelesTriangle, Circle))
print(issubclass(EquilateralTriangle, Circle))

print(issubclass(Parallelogram, Circle))
print(issubclass(Rectangle, Circle))
print(issubclass(Square, Circle))

# TEST_6:
print("\nтест 6")
print(issubclass(Square, Shape))
print(issubclass(IsoscelesTriangle, Shape))
print(issubclass(EquilateralTriangle, Shape))
print(issubclass(Circle, Shape))
