"""
Квадратный трехчлен — это многочлен вида ax2+bx+c, где a≠0. Например:
x2+1x2−5x+6

Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена

Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена

Класс QuadraticPolynomial должен иметь два метода класса:

    from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c,
                       которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса
                       QuadraticPolynomial, созданный на основе переданных коэффициентов
    from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты
                  a, b и c квадратного трехчлена, записанные через пробел. Метод должен возвращать
                  экземпляр класса QuadraticPolynomial, созданный на основе переданных коэффициентов,
                  предварительно преобразованных в экземпляры класса float

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iter_ob):
        return __class__(*iter_ob)

    @classmethod
    def from_str(cls, string: str):
        return __class__(*map(float, string.split()))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
print('\nтест 2')
polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_3:
print('\nтест 3')
polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)

# TEST_4:
print('\nтест 4')
polynom = QuadraticPolynomial.from_str('-19 40 148')

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_5:
print('\nтест 5')
polynom = QuadraticPolynomial.from_iterable([25, 132, -18])

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_6:
print('\nтест 6')
polynom = QuadraticPolynomial.from_iterable([2.5, 13.2, -1.8])

print(polynom.a)
print(polynom.b)
print(polynom.c)
