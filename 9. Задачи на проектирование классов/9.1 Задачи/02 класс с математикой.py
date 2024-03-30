"""
Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности.
    Экземпляр класса Vector должен создаваться на основе собственных координат:

    a = Vector(1, 2, 3)
    b = Vector(3, 4, 5)
    c = Vector(5, 6, 7, 8)

В качестве неформального строкового представления вектор должен иметь собственные координаты,
    заключенные в круглые скобки:

    print(a)                       # (1, 2, 3)
    print(b)                       # (3, 4, 5)
    print(c)                       # (5, 6, 7, 8)

Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

    print(a + b)                   # (4, 6, 8)
    print(a - b)                   # (-2, -2, -2)
    print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
    print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

а также операции сравнения на равенство и неравенство:

    print(a == Vector(1, 2, 3))    # True
    print(a == Vector(4, 5, 6))    # False

При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено
    исключение ValueError с текстом:

    Векторы должны иметь равную длину
"""
from math import sqrt


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    @staticmethod
    def check(first, second):
        if len(first) != len(second):
            raise ValueError("Векторы должны иметь равную длину")

    def __add__(self, other):
        self.check(self, other)
        return self.__class__(*tuple(map(sum, zip(self.coords, other.coords))))

    def __sub__(self, other):
        self.check(self, other)
        return self.__class__(*tuple(map(lambda x: x[0] - x[1], zip(self.coords, other.coords))))

    def __mul__(self, other):
        self.check(self, other)
        return sum(map(lambda x: x[0] * x[1], zip(self.coords, other.coords)))

    def norm(self):
        return sqrt(sum(map(lambda x: x ** 2, self.coords)))

    def __eq__(self, other):
        self.check(self, other)
        return self.coords == other.coords

    def __repr__(self):
        return repr(self.coords)


# INPUT DATA:

print("\n# TEST_1:")
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector3.norm())

print("\n# TEST_2:")
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 == Vector(1, 2, 3))
print(vector1 == Vector(4, 5, 6))
print(vector1 != vector2)

print("\n# TEST_3:")
vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)

print("\n# TEST_4:")
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

vector3 = vector1 + vector2
vector4 = vector1 - vector2

print(type(vector3))
print(type(vector4))

print("\n# TEST_5:")
vector = Vector(18, 21, 14, 88)
print(vector.norm())

print("\n# TEST_6:")
vector1 = Vector(1, 2)
vector2 = Vector(3, 4, 5)

operations = ['vector1 + vector2', 'vector1 - vector2', 'vector1 * vector2', 'vector1 != vector2']

for operation in operations:
    try:
        eval(operation)
    except ValueError as e:
        print(e)

print("\n# TEST_7:")
coordinates = [(14, 51, 47), (39, 17, 64), (43, 20, 88), (42, 12, 66), (74, 81, 82), (27, 12, 48), (26, 73, 15),
               (88, 46, 70), (45, 35, 20), (31, 100, 51), (36, 71, 28), (33, 51, 46), (60, 62, 76), (74, 92, 58),
               (83, 74, 29), (96, 47, 60), (63, 62, 77), (76, 65, 46), (64, 33, 67), (79, 95, 30)]

for x_, y_, z_ in coordinates:
    vector = Vector(x_, y_, z_)
    print(vector + vector, vector - vector, vector * vector, vector.norm())

print("\n# TEST_8:")
coordinates = [((64, 42, 11), (20, 40, 64)), ((50, 96, 60), (32, 26, 38)), ((46, 95, 64), (23, 70, 78)),
               ((22, 29, 48), (21, 50, 31)), ((40, 50, 19), (95, 37, 78)), ((74, 21, 77), (74, 21, 77)),
               ((55, 33, 88), (55, 33, 88)), ((99, 50, 74), (77, 28, 87)), ((64, 65, 33), (24, 73, 76)),
               ((63, 12, 36), (80, 53, 22)), ((92, 15, 80), (48, 42, 17)), ((84, 65, 80), (72, 15, 46)),
               ((54, 48, 52), (68, 25, 26)), ((37, 93, 12), (16, 76, 42)), ((45, 91, 87), (46, 91, 58)),
               ((33, 74, 85), (13, 20, 36)), ((63, 12, 43), (63, 12, 43)), ((87, 67, 41), (41, 82, 52)),
               ((10, 63, 68), (54, 36, 65)), ((74, 51, 90), (30, 25, 90))]

for coord1, coord2 in coordinates:
    vector1 = Vector(*coord1)
    vector2 = Vector(*coord2)
    print(vector1 == vector2, vector1 != vector2)
