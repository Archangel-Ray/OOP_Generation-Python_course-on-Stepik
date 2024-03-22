"""
Реализуйте класс Shape, описывающий геометрическую фигуру. При создании экземпляра класс должен принимать
    три аргумента в следующем порядке:

    name — название фигуры
    color — цвет фигуры
    area — площадь фигуры

Экземпляр класса Shape должен иметь три атрибута:

    name — название фигуры
    color — цвет фигуры
    area — площадь фигуры

Помимо приведенных выше трех атрибутов, экземпляр класса Shape не должен иметь возможности получить какие-либо
    другие атрибуты.

Также экземпляр класса Shape должен иметь следующее неформальное строковое представление:

<цвет фигуры> <название фигуры> (<площадь фигуры>)

Наконец, экземпляры класса Shape должны поддерживать между собой все операции сравнения с помощью
    операторов ==, !=, >, <, >=, <=. Две фигуры считаются равными, если их площади совпадают.
    Фигура считается больше другой фигуры, если ее площадь больше.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
                должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Shape нет, она может быть произвольной.
"""


class Shape:
    __slots__ = ("name", "color", "area")

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f"{self.color} {self.name} ({self.area})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.area == other.area
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.area < other.area
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.area <= other.area
        else:
            return NotImplemented


# INPUT DATA:

print("\n# TEST_1:")
shape = Shape('triangle', 'red', 12)

print(shape.name)
print(shape.color)
print(shape.area)

print("\n# TEST_2:")
print(Shape('Square', 'Red', 4))

print("\n# TEST_3:")
print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))

print("\n# TEST_4:")
shape = Shape('triangle', 'red', 12)

try:
    shape.perimeter = 9
except AttributeError:
    print('Error')

print("\n# TEST_5:")
figures = ['rectangle', 'square', 'triangle', 'circle', 'hexagon', 'rectangle', 'square', 'triangle', 'circle',
           'hexagon', 'rectangle', 'square', 'triangle', 'circle', 'hexagon', 'rectangle', 'square', 'triangle',
           'circle', 'hexagon']

colors = ['Chartreuse', 'AliceBlue', 'DarkSlateBlue', 'Silver', 'RosyBrown', 'MediumAquaMarine', 'LemonChiffon',
          'LightSalmon', 'Moccasin', 'Indigo', 'DarkViolet', 'MediumOrchid', 'AntiqueWhite', 'Peru', 'DarkOliveGreen',
          'CadetBlue', 'Lime', 'LightBlue', 'OrangeRed', 'Yellow']

areas = [92, 18, 35, 59, 59, 64, 50, 38, 26, 58, 25, 74, 17, 67, 24, 20, 30, 54, 88, 64]

for figure, color_, area_ in zip(figures, colors, areas):
    shape = Shape(figure, color_, area_)
    print(shape)

print("\n# TEST_6:")
shape1 = Shape('rectangle', 'Chartreuse', 92)
shape2 = Shape('square', 'AliceBlue', 18)

print(shape1 == shape2)
print(shape1 != shape2)

print("\n# TEST_7:")
shape1 = Shape('triangle', 'DarkSlateBlue', 35)
shape2 = Shape('circle', 'Silver', 59)

print(shape1 >= shape2)
print(shape1 <= shape2)

print("\n# TEST_8:")
shape1 = Shape('hexagon', 'RosyBrown', 59)
shape2 = Shape('rectangle', 'MediumAquaMarine', 64)

print(shape1 < shape2)
print(shape1 > shape2)

print("\n# TEST_9:")
shape = Shape('square', 'LemonChiffon', 50)
not_supported = [[1, 2], True, (1, 2, 3, 4), 'beegeek', {'name': 'Grace Hopper'}, {18, 22}]

for item in not_supported:
    print(shape == item)
    print(item == shape)

print("\n# TEST_10:")
shape = Shape('square', 'LemonChiffon', 50)

print(shape.__eq__(1))
print(shape.__ne__(1.1))
print(shape.__gt__(range(5)))
print(shape.__lt__([1, 2, 3]))
print(shape.__ge__({4, 5, 6}))
print(shape.__le__({1: 'one'}))
