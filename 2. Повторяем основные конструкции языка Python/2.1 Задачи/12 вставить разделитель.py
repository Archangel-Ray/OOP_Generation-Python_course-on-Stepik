# Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:
#
#     iterable — итерируемый объект
#     delimiter — значение-разделитель
#
# Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable,
# между которыми располагается значение-разделитель delimiter.


def intersperse(iterable, delimiter):
    if iterable:
        iterable = iter(iterable)
        yield next(iterable)
        for x in iterable:
            yield delimiter
            yield x


# INPUT DATA:

# TEST_1:
print(*intersperse([1, 2, 3], 0))

# TEST_2:
inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)

# TEST_3:
print(*intersperse('A', '...'))

# TEST_4:
print(*intersperse(range(5), '>'))

# TEST_5:
iterable_ = iter('Beegeek')

print(*intersperse(iterable_, '+'))

# TEST_6:
iterable_ = iter('Be')

print(*intersperse(iterable_, '---'))

# TEST_7:
print(*intersperse([], 100))

# TEST_8:
print(*intersperse('beegeek', '   '))

# TEST_9:
data = intersperse(range(5), -1)
print(list(data))

# TEST_10:
data = intersperse(range(5), '!!!')
print(list(data))

# TEST_11:
data = intersperse(['John Warner Backus', 5, 'Niklaus Emil Wirth', True, 'Lawrence Gordon Tesler', None, {1, 2, 3},
                    {'hello': 'world'}], '—')
print(list(data))
