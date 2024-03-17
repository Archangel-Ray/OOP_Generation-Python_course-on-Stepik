"""
Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении.
    При создании экземпляра класс должен принимать один аргумент:

    iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка.
                Если не передан, начальный набор элементов считается пустым

Класс SortedList должен иметь три метода экземпляра:

    add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
    discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра
                класса SortedList, если он в нем присутствует
    update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы
                в экземпляр класса SortedList

Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(),
    при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.

Экземпляр класса SortedList должен иметь следующее формальное строковое представление:

SortedList([<первый элемент списка>, <второй элемент списка>, ...])

При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем.
    При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено
    исключение NotImplementedError.

Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
    например, с помощью цикла for.

Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов
    с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента
    по его индексу должно быть возбуждено исключение NotImplementedError.

Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:

    оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей
        сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
    оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей
        сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList

Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n
    с помощью операторов * и *=:

    оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой.
        Результатом работы оператора должен являться новый экземпляр класса SortedList
    оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой.
        Результатом работы оператора должен являться левый экземпляр класса SortedList

Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.

Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен
                в качестве родительского.

Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан.
                Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться
                не должен.

Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию
                сравнения, должен вернуть константу NotImplemented.

Примечание 5. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако
            попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее.
"""
from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=()):
        self.data = sorted(iterable)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        del self.data[key]

    @staticmethod
    def add_one(obj, iteration):
        if iteration[0] >= obj:
            iteration.insert(0, obj)
        if iteration[-1] <= obj:
            iteration.append(obj)
        if iteration[0] < obj < iteration[-1]:
            for i in range(len(iteration)):
                if iteration[i] > obj:
                    iteration.insert(i, obj)
                    break
        return iteration

    def add(self, obj, where=None):
        flag = False
        returner = where
        if where is None:
            returner = self.data
        else:
            flag = True
        if isinstance(obj, (int, float)):
            returner = self.add_one(obj, returner)
        if hasattr(obj, "__iter__"):
            for x in obj:
                returner = self.add_one(x, returner)
        if flag:
            return returner

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return SortedList(self.add(other, self.data[:]))
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.add(other)
            return self
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            if other > 0:
                returner = self.data[:]
            else:
                returner = []
            is_added = self.data[:]
            for _ in range(other - 1):
                returner = self.add(is_added, returner)
            return SortedList(returner)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            if other > 0:
                is_added = self.data[:]
                for _ in range(other - 1):
                    self.add(is_added)
            else:
                self.data.clear()
            return self
        else:
            return NotImplemented

    def discard(self, obj):
        while obj in self.data:
            self.data.remove(obj)

    def update(self, it):
        self.add(it)

    def append(self, item):
        raise NotImplementedError

    def insert(self, i, item):
        raise NotImplementedError

    def extend(self, other):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{type(self).__name__}({self.data.__repr__()})'

    def __len__(self):
        return len(self.data)

    def __reversed__(self):
        raise NotImplementedError


print("\n# TEST_1:")
numbers = SortedList([5, 3, 4, 2, 1])

print(numbers)
print(numbers[1])
print(numbers[-2])
numbers.add(0)
print(numbers)
numbers.discard(4)
print(numbers)
numbers.update([4, 6])
print(numbers)

print("\n# TEST_2:")
numbers = SortedList([5, 3, 4, 2, 1])

print(len(numbers))
print(*numbers)
print(1 in numbers)
print(6 in numbers)

print("\n# TEST_3:")
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

print(numbers1 + numbers2)
print(numbers1 * 2)
print(numbers2 * 2)

print("\n# TEST_4:")
numbers = SortedList([5, 4, 3, 2, 1])

print(numbers)
del numbers[1]

print(numbers)
del numbers[-1]

print(numbers)

try:
    numbers[0] = 7
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_5:")
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.append(6)
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_6:")
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.insert(0, 0)
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_7:")
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.extend([6, 7, 8, 9, 10])
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_8:")
numbers = SortedList([1, 2, 3, 4, 5])

try:
    numbers.reverse()
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_9:")
numbers = SortedList([1, 2, 3, 4, 5])

try:
    reversed(numbers)
except NotImplementedError:
    print('Неподдерживаемая операция')

print("\n# TEST_10:")
numbers = SortedList([5, 4, 3, 2, 1])

numbers.update([5, 4, 3, 2, 1])
print(*numbers)

numbers *= 3
print(*numbers)

numbers.discard(4)
print(*numbers)

print("\n# TEST_11:")
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

print("\n# TEST_12:")
data = [5, 4, 3, 2, 1]
numbers = SortedList(data)

print(numbers)
data.pop()

print(data)
print(numbers)

print("\n# TEST_13:")
numbers = SortedList()
print(numbers)

print("\n# TEST_14:")
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 + numbers2
print(numbers1, type(numbers1))

numbers2 = numbers2 * 2
print(numbers2, type(numbers2))

print("\n# TEST_15:")
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 += numbers2
print(numbers1, type(numbers1))

numbers2 *= 2
print(numbers2, type(numbers2))

print("\n# TEST_16:")
numbers1 = SortedList([5, 3, 4, 2, 1])
numbers2 = SortedList([10, 9, 8, 7, 6])

numbers1 = numbers1 * -100
print(numbers1)

numbers2 *= 0
print(numbers2)

print("\n# TEST_17:")
numbers = SortedList([5, 3, 4, 2, 1])
print(numbers.__add__(1))
print(numbers.__iadd__(1.1))
print(numbers.__mul__([1, 2, 3]))
print(numbers.__imul__({4, 5, 6}))
