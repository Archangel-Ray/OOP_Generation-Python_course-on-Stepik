"""
Реализуйте класс ModularTuple, наследника класса tuple, описывающий кортеж, элементы которого во время создания
    автоматически делятся с остатком на заданное число. При создании экземпляра класс должен принимать два аргумента
    в следующем порядке:

    iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса ModularTuple.
                Если не передан, начальный набор элементов считается пустым
    size — целое число, на которое делятся с остатком все элементы создаваемого экземпляра класса ModularTuple,
            по умолчанию имеет значение 100

Примечание 1. Экземпляр класса ModularTuple не должен зависеть от итерируемого объекта, на основе которого он был
                создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса ModularTuple
                измениться  не должен.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса ModularTuple нет, она может быть произвольной.
"""


class ModularTuple(tuple):
    def __new__(cls, iterable=tuple(), size=100):
        return super().__new__(cls, map(lambda x: x % size, iterable[:]))


# INPUT DATA:

# TEST_1:
print("\nтест 1")
modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))

# TEST_2:
print("\nтест 2")
modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)

# TEST_3:
print("\nтест 3")
modulartuple = ModularTuple()
print(modulartuple)

# TEST_4:
print("\nтест 4")
modulartuple = ModularTuple([1, 2, 3, 4, 5], 1)

print(modulartuple)

# TEST_5:
print("\nтест 5")
data = [1, 2, 3, 4, 5]
modulartuple = ModularTuple(data, -5)

print(modulartuple)

data.extend([6, 7, 8, 9, 10])
print(data)
print(modulartuple)
