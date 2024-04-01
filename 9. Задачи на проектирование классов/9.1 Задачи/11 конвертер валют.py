"""
Реализуйте класс Currency для работы со значениями в различных валютах. Экземпляр класса Currency должен создаваться
    на основе числового значения и валюты:

    money1 = Currency(10, 'EUR')
    money2 = Currency(10.0, 'EUR')
    money3 = Currency(20.48, 'USD')
    money4 = Currency(30.3, 'RUB')

Поддерживаемые валюты: EUR (евро), USD (доллар) и RUB (рубль).

В качестве неформального строкового представления экземпляр класса Currency должен иметь собственное числовое значение,
    округленное до двух знаков после запятой, и валюту:

    print(money1)                                      # 10.0 EUR
    print(money2)                                      # 10.0 EUR
    print(money3)                                      # 20.48 USD
    print(money4)                                      # 30.3 RUB

Экземпляр класса Currency должен поддерживать операцию конвертации в другую валюту с помощью метода change_to():

    money1.change_to('RUB')
    print(money1)                                      # 900.0 RUB

Экземпляры класса Currency должны поддерживать между собой операции сложения, вычитания, умножения и деления с помощью
    операторов +, -, * и / соответственно:

    print(Currency(5, 'EUR') + Currency(5, 'EUR'))     # 10.0 EUR
    print(Currency(5, 'EUR') + Currency(11, 'USD'))    # 15.0 EUR
    print(Currency(5, 'RUB') + Currency(11, 'USD'))    # 905.0 RUB
    print(Currency(5, 'USD') * Currency(5, 'EUR'))     # 27.5 USD

Обратите внимание, результирующую валюту должен определять левый операнд.

Примечание 1. Таблица курсов валют:
    1 EUR 	90 RUB
    1 EUR 	1.1 USD
"""


class Currency:
    exchange_rate_table = {'RUB': {'RUB': 1, 'EUR': 1 / 90, 'USD': 1 / (90 / 1.1)},
                           'EUR': {'RUB': 90, 'EUR': 1, 'USD': 1.1},
                           'USD': {'RUB': 90 / 1.1, 'EUR': 1.1, 'USD': 1}}

    def __init__(self, money, currency):
        self.money = float(money)
        self.currency = currency

    def __str__(self):
        return f"{round(self.money, 2)} {self.currency}"

    def change_to(self, currency):
        self.money = self.money * self.exchange_rate_table[self.currency][currency]
        self.currency = currency

    def check(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

    def __add__(self, other):
        self.check(other)
        money = other.money * self.exchange_rate_table[other.currency][self.currency]
        return self.__class__(self.money + money, self.currency)

    def __sub__(self, other):
        self.check(other)
        money = other.money * self.exchange_rate_table[other.currency][self.currency]
        return self.__class__(self.money - money, self.currency)

    def __mul__(self, other):
        self.check(other)
        money = other.money * self.exchange_rate_table[other.currency][self.currency]
        return self.__class__(self.money * money, self.currency)

    def __truediv__(self, other):
        self.check(other)
        money = other.money * self.exchange_rate_table[other.currency][self.currency]
        return self.__class__(self.money / money, self.currency)


# INPUT DATA:

print("\n# TEST_1:")
money1 = Currency(10, 'EUR')
money2 = Currency(20, 'USD')
print(money1)
print(money2)

print("\n# TEST_2:")
money_ = Currency(10, 'EUR')

money_.change_to('RUB')
print(money_)

print("\n# TEST_3:")
print(Currency(5, 'EUR') + Currency(5, 'EUR'))
print(Currency(11, 'USD') - Currency(5, 'EUR'))
print(Currency(5, 'RUB') * Currency(11, 'USD'))
print(Currency(5, 'USD') / Currency(5, 'EUR'))

print("\n# TEST_4:")
money_ = Currency(100, 'USD')
print(money_)

money_.change_to('RUB')
print(money_)

money_.change_to('EUR')
print(money_)

money_.change_to('USD')
print(money_)

print("\n# TEST_5:")
money_ = Currency(2000, 'RUB')
currencies = ['EUR', 'USD', 'RUB']
operation_funcs = ['__sub__', '__mul__', '__add__', '__truediv__']
operation_signs = ['-', '*', '+', '/']
currency_ = 0
operation = 0

values = [46, 54, 18, 81, 16, 86, 40, 82, 31, 74, 82, 39, 72, 40, 16, 72, 16, 24, 74, 30, 37, 87, 67, 95, 54, 79, 86,
          69, 44, 24, 92, 22, 80, 10, 46, 93, 10, 81, 43, 30, 12, 80, 99, 77, 89, 71, 55, 93, 77, 70, 26, 38, 16, 49,
          34, 33, 98, 22, 13, 79, 67, 99, 48, 97, 38, 96, 43, 72, 64, 74, 97, 52, 96, 86, 37, 36, 52, 63, 43, 13, 39,
          43, 52, 33, 92, 56, 17, 20, 94, 21, 28, 57, 96, 77, 99, 88, 38, 28, 70, 59]

for value in values:
    money_.change_to(currencies[currency_ % 3])
    current_currency = currency_ % 3 - 1
    current_operation = operation % 4
    print(f'{money_} {operation_signs[current_operation]} {value} {currencies[current_currency]} = ', end='')
    print(Currency.__dict__[operation_funcs[current_operation]](money_, Currency(value, currencies[current_currency])))
    currency_ += 1
    operation += 1
