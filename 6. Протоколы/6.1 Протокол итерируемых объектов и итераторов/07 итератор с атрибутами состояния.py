"""
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:

    iterable — итерируемый объект

Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable
    в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

    accesses — свойство, доступное только для чтения, возвращающее количество элементов,
                сгенерированных итератором на данный момент
    empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить
                        следующий элемент опустевшего итератора
    first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его.
                Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта,
                то должно быть возбуждено исключение AttributeError с текстом:

                Исходный итерируемый объект пуст

    last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором
            на данный момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено
            исключение AttributeError с текстом:

            Последнего элемента нет

Класс LoopTracker должен иметь один метод экземпляра:

    is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь
                методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
"""


class LoopTracker:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.__accesses = 0
        self.__empty_accesses = 0
        self.__first = self.iterable[0] if self.iterable else None
        self.__last = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            self.__accesses += 1
            self.__last = self.iterable.pop(0)
            return self.__last
        else:
            self.__empty_accesses += 1
            raise StopIteration

    @property
    def accesses(self):
        return self.__accesses

    @property
    def empty_accesses(self):
        return self.__empty_accesses

    @property
    def first(self):
        if self.__first is not None:
            return self.__first
        else:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.__last:
            return self.__last
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        if self.iterable:
            return False
        return True


# INPUT DATA:

# TEST_1:
print('\nтест 1')
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))

# TEST_2:
print('\nтест 2')
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

# TEST_3:
print('\nтест 3')
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

# TEST_4:
print('\nтест 4')
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

# TEST_5:
print('\nтест 5')
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass

print(loop_tracker.empty_accesses)

# TEST_6:
print('\nтест 6')
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())

# TEST_7:
print('\nтест 7')
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))

# TEST_8:
print('\nтест 8')
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
print('\nтест 9')
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
print('\nтест 10')
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)

# TEST_11:
print('\nтест 11')
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_12:
print('\nтест 12')
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())

# TEST_13:
print('\nтест 13')
loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))
