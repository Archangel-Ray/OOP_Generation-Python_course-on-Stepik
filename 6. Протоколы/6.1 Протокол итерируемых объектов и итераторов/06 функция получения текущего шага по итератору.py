"""
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:

    iterable — итерируемый объект

Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable
    в исходном порядке, а затем возбуждает исключение StopIteration.

Класс Peekable должен иметь один метод экземпляра:

    peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий
                итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен
                уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо
                возбуждения исключения StopIteration, если итератор пуст

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
                Реализация же протокола может быть произвольной.
"""
from itertools import islice


class Peekable:
    def __init__(self, arg):
        self.iterable = list(iter(arg))

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            return self.iterable.pop(0)
        raise StopIteration

    def peek(self, default=StopIteration):
        if self.iterable:
            return self.iterable[0]
        if default is StopIteration:
            raise StopIteration
        else:
            return default


# INPUT DATA:

# TEST_1:
print('\nтест 1')
iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)

# TEST_2:
print('\nтест 2')
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# TEST_3:
print('\nтест 3')
iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))

# TEST_4:
print('\nтест 4')
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')

# TEST_5:
print('\nтест 5')
iterator = Peekable([n ** 2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))

# TEST_6:
print('\nтест 6')
iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))

# TEST_7:
print('\nтест 7')
iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')
