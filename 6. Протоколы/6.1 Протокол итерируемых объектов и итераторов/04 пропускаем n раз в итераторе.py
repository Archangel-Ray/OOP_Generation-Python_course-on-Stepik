"""
Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — целое неотрицательное число

Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable,
    пропуская по n элементов, а затем возбуждает исключение StopIteration.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__().
                Реализация же протокола может быть произвольной.
"""


class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n
        self.ending = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.ending:
            raise StopIteration
        returnable = next(self.iterable)
        try:
            for _ in range(self.n):
                next(self.iterable)
        except StopIteration:
            self.ending = True
        return returnable


# INPUT DATA:

# TEST_1:
print('\nтест 1')
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)

# TEST_2:
print('\nтест 2')
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)

# TEST_3:
print('\nтест 3')
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)

# TEST_4:
print('\nтест 4')
skipiterator = SkipIterator('abcd', 0)

print(*skipiterator)

# TEST_5:
print('\nтест 5')
skipiterator = SkipIterator(['abcd'], 1)

print(*skipiterator)

# TEST_6:
print('\nтест 6')
skipiterator = SkipIterator('abcd', 3)

print(*skipiterator)

# TEST_7:
print('\nтест 7')
skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)

# TEST_8:
print('\nтест 8')
skipiterator = SkipIterator(iter(['aa', 'bb', 'cc', 'dd', 'ee', 'ff']), 2)

print(*skipiterator)

# TEST_9:
print('\nтест 9')
data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)

print(*skipiterator)

# TEST_10:
print('\nтест 10')
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))
