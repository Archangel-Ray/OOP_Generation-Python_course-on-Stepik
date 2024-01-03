"""
Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных
    аргументов, каждый из которых является последовательностью. Класс SequenceZip должен описывать последовательность,
    элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи.
    Объединение должно происходить аналогично тому, как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
    например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса SequenceZip не должен зависеть от последовательностей, на основе которых он был создан.
                Другими словами, если исходные последовательности изменятся, то экземпляр класса SequenceZip
                измениться  не должен.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса SequenceZip нет, она может быть произвольной.
"""
from copy import deepcopy


class SequenceZip:
    def __init__(self, *args):
        self.saved_zip = deepcopy(zip(*args))

    def __len__(self):
        length = 0
        for _ in deepcopy(self.saved_zip):
            length += 1
        return length

    def __getitem__(self, item):
        copy_zip = deepcopy(self.saved_zip)
        for _ in range(item):
            next(copy_zip)
        return next(copy_zip)

    def __iter__(self):
        for n in deepcopy(self.saved_zip):
            yield n


# INPUT DATA:

# TEST_1:
print('\nтест 1')
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

# TEST_2:
print('\nтест 2')
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

# TEST_3:
print('\nтест 3')
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

# TEST_4:
print('\nтест 4')
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

# TEST_5:
print('\nтест 5')
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# TEST_6:
print('\nтест 6')
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# TEST_7:
print('\nтест 7')
data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))
