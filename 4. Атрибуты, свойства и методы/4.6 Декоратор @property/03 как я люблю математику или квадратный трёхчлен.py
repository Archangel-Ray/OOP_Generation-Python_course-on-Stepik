"""
Квадратный трехчлен – это многочлен вида ax2+bx+c, где a≠0. Например:

x2+1
x2−5x+6

Значение переменной x, при котором квадратный трехчлен обращается в ноль, называют его корнем.
Квадратный трехчлен может иметь один корень, два корня или вовсе не иметь корней.
Корни квадратного трехчлена, если они существуют, находятся по формуле:

x1,2=(−b±√b2−4ac)/2a

​​Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:

    a — коэффициент a квадратного трехчлена
    b — коэффициент b квадратного трехчлена
    c — коэффициент c квадратного трехчлена

Экземпляр класса QuadraticPolynomial должен иметь три атрибута:

    a — коэффициент aa квадратного трехчлена
    b — коэффициент bb квадратного трехчлена
    c — коэффициент cc квадратного трехчлена

Класс QuadraticPolynomial должен иметь четыре свойства:

    x1 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:
    x1=(−b−√b2−4ac)/2a
    ​​Если квадратный трехчлен не имеет корней (b2−4ac<0), значением свойства должно быть значение None

    x2 — свойство, доступное только для чтения, возвращающее корень квадратного трехчлена, вычисленный по формуле:
    x2=(−b+√b2−4ac)/2a
    ​​Если квадратный трехчлен не имеет корней (b2−4ac<0b2−4ac<0), значением свойства должно быть значение None

    view — свойство, доступное только для чтения, возвращающее строку вида:
    ax^2 + bx + c
    где a, b и с представляют коэффициенты квадратного трехчлена

    coefficients — свойство, доступное для чтения и записи, возвращающее кортеж вида:
    (a, b, c)
    где a, b и с представляют коэффициенты квадратного трехчлена

Примечание 1. Если квадратный трехчлен имеет лишь один корень, значения свойств x1 и x2 должны совпадать.

Примечание 2. При изменении коэффициентов квадратного трехчлена через соответствующие атрибуты
              или свойство coefficients значения свойств x1, x2, view и coefficients также должны изменяться.

Примечание 3. Если какие-либо коэффициенты квадратного трехчлена равны нулю, они по-прежнему должны
              присутствовать в строке, возвращаемой свойством view, дополнительно их убирать не нужно.

Примечание 4. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 5. Никаких ограничений касательно реализации класса QuadraticPolynomial нет, она может быть произвольной.
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def discriminant(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, args):
        self.a, self.b, self.c = args

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def x1(self):
        if self.discriminant >= 0:
            return (-self.b - self.discriminant ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.discriminant >= 0:
            return (-self.b + self.discriminant ** 0.5) / (2 * self.a)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
print('\nтест 2')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

# TEST_3:
print('\nтест 3')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

# TEST_4:
print('\nтест 4')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_5:
print('\nтест 5')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_6:
print('\nтест 6')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_7:
print('\nтест 7')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_8:
print('\nтест 8')
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_9:
print('\nтест 9')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
