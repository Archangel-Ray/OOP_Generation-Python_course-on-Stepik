"""
ДНК состоит из двух цепей, ориентированных азотистыми основаниями друг к другу. В ДНК встречается четыре вида
    азотистых оснований: аденин (A), гуанин (G), тимин (T) и цитозин (C). Азотистые основания одной из цепей
    соединены с азотистыми основаниями другой цепи водородными связями согласно принципу комплементарности:
    аденин (A) соединяется только с тимином (T), гуанин (G) — только с цитозином (C).

Реализуйте класс DNA, описывающий двухцепочную спираль ДНК.
    При создании экземпляра класс должен принимать один аргумент:

    chain — первая цепь ДНК, представляющая собой строку из символов A, G, T и C (азотистых оснований)

Экземпляр класса DNA должен иметь следующее неформальное строковое представление:

    <азотистые основания первой цепи ДНК>

При передаче экземпляра класса DNA в функцию len() должно возвращаться количество азотистых оснований
    в одной из его цепей. При передаче экземпляра класса в функцию reversed() должен возвращаться итератор,
    элементами которого являются элементы переданного экземпляра класса DNA, расположенные в обратном порядке.

Помимо этого, экземпляр класса DNA должен быть итерируемым объектом, то есть позволять перебирать свои элементы,
    например, с помощью цикла for.

Также экземпляр класса DNA должен позволять получать значения своих элементов с помощью индексов,
    причем как положительных, так и отрицательных.

В случае с функцией reversed(), итерацией и доступу по индексам элементы экземпляра класса DNA должны быть
    представлены в виде кортежей из двух элементов, первым из которых является основание первой цепи ДНК
    по указанному индексу, вторым — азотистое основание второй цепи ДНК по указанному индексу.
    Азотистое основание второй цепи ДНК можно получить при помощи принципа комплементарности.

Вдобавок ко всему, экземпляр класса DNA должен поддерживать операцию проверки на принадлежность с помощью оператора in.
    В данном случае должно проверяться, входит ли азотистое основание в первую цепь ДНК.

Экземпляры класса DNA должны поддерживать между собой операции сравнения с помощью операторов == и!=.
    Две ДНК считаются равными, если их первые цепи совпадают.

Наконец, экземпляры класса DNA должны поддерживать между собой операцию сложения с помощью оператора +,
    результатом которой должен являться новый экземпляр класса DNA, первой цепью которого является конкатенация
    первых цепей исходных экземпляров класса DNA.

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве
                родительского.

Примечание 2. Если объект, с которым выполняется операция сравнения или сложения, некорректен, метод,
                реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса DNA нет, она может быть произвольной.
"""
from collections import UserString


class DNA(UserString):
    of_nitrogenous_bases = {'A': ('A', 'T'), 'T': ('T', 'A'), 'G': ('G', 'C'), 'C': ('C', 'G')}

    def __init__(self, chain):
        self.data = chain

    def __getitem__(self, item):
        return self.of_nitrogenous_bases[self.data[item]]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, DNA):
            return self.__class__(self.data + other.data)
        else:
            return NotImplemented


# INPUT DATA:

print("\n# TEST_1:")
dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])

print("\n# TEST_2:")
dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)

print("\n# TEST_3:")
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))

print("\n# TEST_4:")
dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)

print("\n# TEST_5:")
dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

print(*dna)
print(*reversed(dna))
print('A' in dna)
print('C' not in dna)

print("\n# TEST_6:")
dna = DNA('ACG')
not_supported = [1, 2.23, [1, 2, 3], {1: 'one'}, {4, 5, 6}, True, False, 'CTA', (7, 8, 9)]

for item_ in not_supported:
    print(item_ == dna)

print("\n# TEST_7:")
dnas = ['TAAAACCCCATCGGCTCTGACAATGAAC', 'AGATGTTCCCTCTAATATCTATACGAAT', 'ACGACGCACTGCATACAATACAATAGTG',
        'TCCCAGTCAGGATCGGATTGGTATAATC', 'TACACGCATAGTGCCCAACTCCTACCCG', 'TCACCGCTGAAAACATGTTCTGGAGGGC',
        'CCCAGGATAGACCTATTTGCCGTATCCA', 'ATCGATCGTGCGGGAAATCCTGCCATAT', 'AGACCAACTTATTGGGCACACGCTCCGG',
        'CGCGTCCCCCATATCAACGCGTGAATGC', 'AGTCACGATCAGCTGGACGTAGTGGCAA', 'GTGTAGGGTCAAGGGACACCTGATATCT',
        'AAAAGACGAAAATTGCTAAGTGGCAGTC', 'TGGAGGCCGAGCTCGCGTTGGAAATAGT', 'AAGTCTGCCGAGGCGGGTCGGGAGCGCC',
        'ATTATCCAATCCAGTCACGTATTGAATA', 'ATTGTGAACCTTATACGTTAGTAATACC', 'AGACAATCATGCTATTAGGTATGACGTT',
        'ATCACTGAGGCAGAGACTAGCCGCGCTT', 'TATGGGTGGTATCCTAAGCATTCAATGG']

for base in dnas:
    dna = DNA(base)
    print(*dna)

print("\n# TEST_8:")
dna = DNA('ACG')
print(dna.__eq__(1))
print(dna.__ne__(1.1))
print(dna.__add__([1, 2, 3]))
