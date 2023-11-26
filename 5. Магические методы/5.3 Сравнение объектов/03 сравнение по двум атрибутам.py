"""
Реализуйте класс Month, описывающий месяц.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:

    year — год
    month — порядковый номер месяца

Экземпляр класса Month должен иметь следующее формальное строковое представление:

Month(<год>, <порядковый номер месяца>)

И следующее неформальное строковое представление:

<год>-<порядковый номер месяца>

Также экземпляры класса Month должны поддерживать все операции сравнения с помощью операторов
==, !=, >, <, >=, <=. Два Month объекта считаются равными, если их годы и порядковые номера месяцев совпадают.
Month объект считается больше другого Month объекта, если его год больше. В случае если два Month объекта имеют
равные года, большим считается тот, чей месяц больше. Методы, реализующие операции сравнения, должны уметь сравнивать
как два Month объекта между собой, так и Month объект с кортежем из двух чисел, представляющих год и месяц.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию,
должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Month нет, она может быть произвольной.
"""
from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year_, month_):
        self.year = year_
        self.month = month_

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        if isinstance(other, tuple):
            return (self.year, self.month) == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        if isinstance(other, tuple):
            return (self.year, self.month) < other
        else:
            return NotImplemented

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

# TEST_2:
print("\nтест 2")
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))

# TEST_3:
print("\nтест 3")
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))

# TEST_4:
print("\nтест 4")
month = Month(2023, 4)
not_supported = ['04.2023', 4.0, 2023, True, {2023: 4}, {4, 2023}, False, (2023, 4, 'dont know')]
for obj in not_supported:
    print(month == obj)

# TEST_5:
print("\nтест 5")
months = [Month(2014, 4), Month(2016, 8), Month(2006, 5), Month(2022, 8), Month(2014, 9), Month(2014, 9),
          Month(2002, 12), Month(2003, 8), Month(2016, 5), Month(2022, 5), Month(2019, 12), Month(2011, 2),
          Month(2005, 12), Month(2009, 8), Month(2023, 2), Month(2020, 5), Month(2020, 6), Month(2022, 4),
          Month(2000, 12), Month(2002, 5), Month(2012, 4), Month(2007, 1), Month(2008, 4), Month(2008, 1),
          Month(2000, 11), Month(2006, 8), Month(2011, 9), Month(2012, 12), Month(2015, 9), Month(2017, 12),
          Month(2016, 5), Month(2002, 1), Month(2015, 8), Month(2003, 4), Month(2005, 9), Month(2016, 9),
          Month(2009, 12), Month(2017, 4), Month(2020, 3), Month(2018, 12), Month(2008, 1), Month(2011, 11),
          Month(2004, 9), Month(2004, 9), Month(2002, 5), Month(2014, 6), Month(2023, 5), Month(2016, 11),
          Month(2002, 8), Month(2005, 12), Month(2002, 7), Month(2008, 3), Month(2015, 4), Month(2010, 10),
          Month(2014, 7), Month(2022, 9), Month(2001, 11), Month(2003, 1), Month(2000, 4), Month(2012, 7),
          Month(2004, 1), Month(2011, 6), Month(2012, 8), Month(2008, 9), Month(2005, 2), Month(2007, 8),
          Month(2012, 1), Month(2018, 7), Month(2022, 12), Month(2018, 11), Month(2001, 5), Month(2009, 10),
          Month(2000, 8), Month(2008, 4), Month(2018, 10), Month(2003, 5), Month(2020, 12), Month(2011, 3),
          Month(2003, 12), Month(2023, 3), Month(2003, 1), Month(2020, 7), Month(2019, 4), Month(2020, 2),
          Month(2005, 11), Month(2008, 7), Month(2013, 9), Month(2015, 4), Month(2004, 12), Month(2001, 2),
          Month(2003, 9), Month(2021, 6), Month(2020, 9), Month(2000, 10), Month(2021, 4), Month(2014, 11),
          Month(2016, 9), Month(2004, 12), Month(2015, 10), Month(2009, 1)]

print(sorted(months))
print(min(months))
print(max(months))

# TEST_6:
print("\nтест 6")
print(Month(1999, 12) == (1999, 12))
print(Month(1999, 12) < (2000, 1))
print(Month(1999, 12) > (2000, 1))
print(Month(1999, 12) <= (1999, 12))
print(Month(1999, 12) >= (2000, 1))

# TEST_7:
print("\nтест 7")
month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: 'one'}))
