"""
Назовем диапазоном запись двух целых неотрицательных чисел через дефис a-b, где a — левая граница диапазона,
    b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a до b включительно.
    Например, диапазон 1-4 содержит числа 1, 2, 3 и 4.

Реализуйте класс CustomRange, описывающий последовательность, элементами которой являются одиночные целые числа и
    числа из определенных диапазонов. При создании экземпляра класс должен принимать произвольное количество
    позиционных аргументов, каждый из которых является одиночным целым числом либо диапазоном.

При передаче экземпляра класса CustomRange в функцию len() должно возвращаться количество элементов в нем.
    При передаче экземпляра класса CustomRange в функцию reversed() должен возвращаться итератор, элементами
    которого являются элементы переданного экземпляра класса CustomRange, расположенные в обратном порядке.

Экземпляр класса CustomRange должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
    например, с помощью цикла for.

Помимо этого, экземпляр класса CustomRange должен поддерживать операцию проверки на принадлежность
    с помощью оператора in.

Наконец, экземпляр класса CustomRange должен позволять получать значения своих элементов с помощью индексов,
    причем как положительных, так и отрицательных

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен
                в качестве родительского.

Примечание 2. Реализация класса CustomRange может быть произвольной,
                то есть требований к наличию определенных атрибутов нет.

Примечание 3. Дополнительная проверка данных на корректность в методах не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.
"""
from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.it = []
        for x in args:
            if isinstance(x, int):
                self.it.append(x)
            elif isinstance(x, str):
                diapason = x.split("-")
                self.it.extend([el for el in range(int(diapason[0]), int(diapason[1]) + 1)])

    def __getitem__(self, item):
        return self.it[item]

    def __len__(self):
        return len(self.it)


# INPUT DATA:

print("\n# TEST_1:")
customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])

print("\n# TEST_2:")
customrange = CustomRange(1, '2-5', 3, '1-4')

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)

print("\n# TEST_3:")
customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))

print("\n# TEST_4:")
customrange = CustomRange('0-1000')

print(len(customrange))
print(*customrange)

print("\n# TEST_5:")
customrange = CustomRange('0-50', '25-75', '50-100')

for digit in customrange:
    print(digit, end=' ')

print("\n# TEST_6:")
customrange = CustomRange(1, 212, '89-323', 87, '17-82', 124, '300-312', 832, 1234)

print(*customrange)
print(customrange[11])
print(customrange[44])
print(customrange[-12])
print(customrange[-38])
print(82 in customrange)
print(17 in customrange)
