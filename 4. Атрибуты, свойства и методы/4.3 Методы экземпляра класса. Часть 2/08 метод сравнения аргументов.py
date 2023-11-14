"""
Реализуйте класс Scales, описывающий весы с двумя чашами.
При создании экземпляра класс не должен принимать никаких аргументов.

Класс Scales должен иметь три метода экземпляра:

    add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и
    добавляющий на правую чашу весов этот груз
    add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и
    добавляющий на левую чашу весов этот груз
    get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах совпадают,
    Правая чаша тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая чаша тяжелее

Примечание 1. Пустые весы всегда находятся в равновесии.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, weight):
        self.right += weight

    def add_left(self, weight):
        self.left += weight

    def get_result(self):
        if self.right < self.left:
            return 'Левая чаша тяжелее'
        elif self.right > self.left:
            return 'Правая чаша тяжелее'
        else:
            return 'Весы в равновесии'


scales = Scales()

scales.add_right(1)
scales.add_right(2)
scales.add_left(2)

print(scales.get_result())
