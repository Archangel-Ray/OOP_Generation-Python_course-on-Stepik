"""
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:
код страны 	формат даты
ru 	DD.MM.YYYY
us 	MM-DD-YYYY
ca 	YYYY-MM-DD
br 	DD/MM/YYYY
fr 	DD.MM.YYYY
pt 	DD-MM-YYYY

Реализуйте класс DateFormatter, экземпляры которого позволяют преобразовывать даты в формат определенной страны из
таблицы выше. При создании экземпляра класс должен принимать один аргумент:

    country_code — код страны

Экземпляр класса DateFormatter должен являться вызываемым объектом и принимать один аргумент:

    d — дата (тип date)

Экземпляр класса DateFormatter должен возвращать строку с датой d в формате страны с кодом country_code.

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса DateFormatter нет, она может быть произвольной.
"""
from datetime import date


class DateFormatter:
    def __init__(self, country_code):
        self.country_code = {'ru': '%d.%m.%Y',
                             'us': '%m-%d-%Y',
                             'ca': '%Y-%m-%d',
                             'br': '%d/%m/%Y',
                             'fr': '%d.%m.%Y',
                             'pt': '%d-%m-%Y'}[country_code]

    def __call__(self, date_):
        return date_.strftime(self.country_code)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

# TEST_2:
print('\nтест 2')
us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

# TEST_3:
print('\nтест 3')
ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))

# TEST_4:
print('\nтест 4')
br_format = DateFormatter('br')

print(br_format(date(2022, 11, 7)))

# TEST_5:
print('\nтест 5')
fr_format = DateFormatter('fr')

print(fr_format(date(2022, 11, 7)))

# TEST_6:
print('\nтест 6')
pt_format = DateFormatter('pt')

print(pt_format(date(2022, 11, 7)))

# TEST_7:
print('\nтест 7')
formats = ('ru', 'fr', 'us', 'ca', 'br', 'pt')
dates = [date(1981, 5, 26), date(2004, 6, 26), date(2000, 4, 26), date(1983, 2, 19), date(1981, 11, 9),
         date(2019, 11, 24), date(2022, 3, 24), date(1996, 7, 11), date(1971, 6, 9), date(2021, 5, 22),
         date(1994, 10, 13), date(2002, 7, 10), date(1981, 11, 28), date(2019, 1, 8), date(2011, 2, 23),
         date(1998, 1, 17), date(2006, 2, 19), date(1987, 6, 17), date(1995, 2, 15), date(2020, 3, 8),
         date(2015, 4, 16), date(1987, 11, 26), date(1971, 12, 17), date(1984, 12, 21), date(1977, 1, 7),
         date(2012, 2, 20), date(2017, 9, 2), date(1971, 5, 23), date(2010, 8, 23), date(1973, 2, 19),
         date(1980, 11, 24), date(1986, 3, 31), date(2005, 5, 21), date(2001, 5, 9), date(2022, 7, 10),
         date(1995, 9, 27), date(1976, 2, 29), date(2002, 5, 24), date(2016, 10, 25), date(2018, 11, 17),
         date(1986, 5, 1), date(1970, 3, 14), date(1987, 2, 19), date(1976, 10, 10), date(2000, 4, 11),
         date(2008, 9, 28), date(1986, 3, 26), date(1988, 3, 10), date(2016, 1, 26), date(2017, 3, 1),
         date(2008, 11, 2), date(1980, 3, 31), date(1979, 3, 10), date(1985, 2, 17), date(1983, 1, 16),
         date(1977, 10, 2), date(1971, 6, 21), date(2011, 11, 7), date(1970, 3, 5), date(2006, 4, 5),
         date(1999, 2, 3), date(1981, 10, 2), date(1999, 6, 13), date(1973, 9, 27), date(2003, 7, 4),
         date(1992, 1, 1), date(2007, 12, 7), date(2003, 4, 10), date(2014, 4, 4), date(1982, 8, 6),
         date(2005, 11, 24), date(1980, 5, 17), date(2022, 6, 15), date(1986, 6, 1), date(2011, 9, 7),
         date(2018, 7, 18), date(2004, 8, 20), date(2010, 2, 8),
         date(2008, 2, 18), date(1987, 10, 1), date(2022, 2, 7), date(1979, 9, 18), date(1976, 9, 6), date(1990, 6, 11),
         date(1991, 5, 17), date(1974, 10, 16), date(1977, 3, 29), date(1989, 10, 14), date(2010, 12, 17),
         date(2001, 1, 21), date(1971, 8, 25), date(1986, 5, 6), date(1979, 8, 25), date(1984, 3, 28),
         date(1971, 11, 4), date(1973, 6, 11), date(1986, 4, 13), date(2003, 2, 7), date(1977, 9, 26),
         date(2003, 11, 28)]

count = 0
for d in dates:
    format_code = DateFormatter(formats[count % len(formats)])
    print(format_code(d))
    count += 1
