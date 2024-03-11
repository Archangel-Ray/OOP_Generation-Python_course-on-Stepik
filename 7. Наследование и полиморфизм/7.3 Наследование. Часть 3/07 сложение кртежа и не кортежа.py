"""
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию
    сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами.
    Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться
                новый экземпляр класса AdvancedTuple.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.
"""


class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(list(self) + list(other))

    def __radd__(self, other):
        return AdvancedTuple(list(other) + list(self))


# INPUT DATA:

# TEST_1:
print("\nтест 1")
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)

# TEST_2:
print("\nтест 2")
advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))

# TEST_3:
print("\nтест 3")
data = [[4, 5, 6], {4: None, 5: None, 6: None}, (4, 5, 6), '456', iter([4, 5, 6]), AdvancedTuple([4, 5, 6])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    print(advancedtuple + item, end=' ')
    print(item + advancedtuple)

# TEST_4:
print("\nтест 4")
data = ['456', [7, 8, 9], {10: None, 11: None, 12: None}, (13, 14, 15), iter([16, 17, 18]), AdvancedTuple([20, 21, 22])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    advancedtuple += item

print(advancedtuple)

# TEST_5:
print("\nтест 5")
advancedtuple = AdvancedTuple([1, 2, 3])
advancedtuple += []
print(advancedtuple)
