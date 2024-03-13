"""
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа.
    При создании экземпляра класс должен принимать один аргумент:

    iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList.
                Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть
                возбуждено исключение TypeError с текстом:

                Элементами экземпляра класса NumberList должны быть числа

    Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым

При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(),
    extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами,
    в противном случае должно возбуждаться исключение TypeError с текстом:

    Элементами экземпляра класса NumberList должны быть числа

Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан.
                Другими словами, если исходный итерируемый объект изменится,
                то экземпляр класса NumberList измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.
"""
from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable):
        if self.check(iterable):
            super().__init__(iterable)

    @staticmethod
    def check(iterable):
        if not iterable:
            return True
        elif isinstance(iterable, (int, float)):
            return True
        elif all([isinstance(x, (int, float)) for x in iterable]):
            return True
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __setitem__(self, index, item):
        self.check(item)
        super().__setitem__(index, item)

    def insert(self, index, item):
        if isinstance(item, (int, float)):
            self.check(item)
            super().insert(index, item)
        else:
            self.check(" ")

    def append(self, item):
        self.check(item)
        super().append(item)

    def extend(self, other):
        self.check(other)
        return super().extend(other)

    def __add__(self, other):
        self.check(other)
        return super().__add__(other)

    def __iadd__(self, other):
        self.check(other)
        return self.__add__(other)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)

# TEST_2:
print("\nтест 2")
numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)

# TEST_3:
print("\nтест 3")
try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)

# TEST_4:
print("\nтест 4")
numberlist = NumberList([1, 2, 3])

try:
    numberlist.append('4')
except TypeError as error:
    print(error)

# TEST_5:
print("\nтест 5")
numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)

# TEST_6:
print("\nтест 6")
numberlist1 = NumberList([1, 2])

try:
    numberlist2 = numberlist1 + [3, '4']
except TypeError as e:
    print(e)

# TEST_7:
print("\nтест 7")
data = [1, 2, 3]
numberlist = NumberList(data)

print(numberlist)

data.extend([4, 5, 6])
print(data)
print(numberlist)

# TEST_8:
print("\nтест 8")
numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)

# TEST_9:
print("\nтест 9")
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, '4', 3])
except TypeError as e:
    print(e)

# TEST_10:
print("\nтест 10")
n = NumberList([1, 2, 3])

try:
    n[1] = '5'
except TypeError as e:
    print(e)
