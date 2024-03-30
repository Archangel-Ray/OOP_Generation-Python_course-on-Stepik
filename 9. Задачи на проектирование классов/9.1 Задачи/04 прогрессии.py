"""
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра
    класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

    progression = ArithmeticProgression(0, 1)

    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10

    Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии.
    При создании экземпляра класса GeometricProgression должны указываться первый член последовательности
    и знаменатель прогрессии:

    progression = GeometricProgression(1, 2)

    for elem in progression:
        if elem > 10:
            break
        print(elem, end=' ')    # 1 2 4 8

    Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.
"""


class Progression:
    def __init__(self, *args):
        self.start = args[0]
        self.step = args[1]


class ArithmeticProgression(Progression):
    def __iter__(self):
        while True:
            yield self.start
            self.start += self.step


class GeometricProgression(Progression):
    def __iter__(self):
        while True:
            yield self.start
            self.start *= self.step


# INPUT DATA:

print("\n\n# TEST_1:")
progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print("\n\n# TEST_2:")
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')

print("\n\n# TEST_3:")
progression = GeometricProgression(4, -2)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print("\n\n# TEST_4:")
progression = ArithmeticProgression(100, -10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')

print("\n\n# TEST_5:")
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')
