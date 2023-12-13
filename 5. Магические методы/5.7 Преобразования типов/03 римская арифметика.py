"""
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления.
    При создании экземпляра класс должен принимать один аргумент:

        number — число в римской системе счисления. Например, IV

Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>

Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому
    его значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой
    все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью
    операторов + и - соответственно:

    результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
    результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных

Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.

Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих
    арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

Примечание 4. Дополнительная проверка данных на корректность не требуется.
    Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса RomanNumeral нет, она может быть произвольной.
"""
from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number_):
        self.number = number_

    def __str__(self):
        return self.number

    def __int__(self):
        roman_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last = roman_arabic[self.number[-1]]
        negative = True
        res = last
        for i in range(2, len(self.number) + 1):
            present_value = roman_arabic[self.number[-i]]
            if last < present_value:
                res += present_value
                negative = True
            elif last == present_value:
                if negative:
                    res += present_value
                else:
                    res -= present_value
            else:
                if negative:
                    res -= present_value
                    negative = False
                else:
                    res += present_value
                    negative = False
            last = present_value
        return res

    @staticmethod
    def arabic_in_roman(numb):
        res = ''
        numb = str(numb)
        for i in range(1, len(numb) + 1):
            if numb[-i] != '0':
                res = ((0, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
                       (0, 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
                       (0, 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                       (0, 'M', 'M'*2, 'M'*3, 'M'*4, 'M'*5, 'M'*6, 'M'*7, 'M'*8, 'M'*9))[i - 1][int(numb[-i])] + res
        return res

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic_in_roman(int(self) + int(other)))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.arabic_in_roman(int(self) - int(other)))
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        else:
            return NotImplemented


# INPUT DATA:

# TEST_1:
print("\nтест 1")
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

# TEST_2:
print("\nтест 2")
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

# TEST_3:
print("\nтест 3")
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
print("\nтест 4")
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
print("\nтест 5")
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_6:
print("\nтест 6")
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V')

print(number)
print(int(number))

# TEST_7:
print("\nтест 7")
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
print("\nтест 8")
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
print("\nтест 9")
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
print("\nтест 10")
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))

print("\nмой тест")
list_of_numbers = []
for x in range(1, 10000):
    list_of_numbers.append(RomanNumeral(RomanNumeral.arabic_in_roman(x)))
for x in list_of_numbers:
    print(f"{int(x)} - {x}")
