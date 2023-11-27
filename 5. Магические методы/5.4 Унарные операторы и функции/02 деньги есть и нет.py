"""
Реализуйте класс Money, описывающий денежную сумму в рублях.
При создании экземпляра класс должен принимать один аргумент:

    amount — количество денег

Экземпляр класса Money должен иметь следующее неформальное строковое представление:

<количество денег> руб.

Также экземпляр класса Money должен поддерживать унарные операторы + и -:

    результатом унарного + должен являться новый экземпляр класса Money с неотрицательным количеством денег
    результатом унарного - должен являться новый экземпляр класса Money с отрицательным количеством денег

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса Money нет, она может быть произвольной.
"""


class Money:
    def __init__(self, amount_):
        self.amount = amount_

    def __str__(self):
        return f'{self.amount} руб.'

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        return Money(-abs(self.amount))


# INPUT DATA:

# TEST_1:
print('\nтест 1')
money = Money(100)

print(money)
print(+money)
print(-money)

# TEST_2:
print('\nтест 2')
money = Money(-100)

print(money)
print(+money)
print(-money)

# TEST_3:
print('\nтест 3')
money = Money(-100)

print(type(money))
print(type(+money))
print(type(-money))

# TEST_4:
print('\nтест 4')
money = Money(500)
neg_money = -money
print(neg_money is money)

# TEST_5:
print('\nтест 5')
amounts = [0, -5983, 2205, 3997, 5343, 3346, -733, -2240, -1195, 9823, 8147, -3380, -4802, -8677, 9380, 2013, 8943, 664,
           -3161, -8467, -5869, -9562, 9830, -8391, -5780, 4600, 5289, -8634, 7982, 1815, -7881, -8572, -1271, 2881,
           -5134, 909, 6641, -480, -581, 7427, 8759, -775, 1363, 9616, -7803, 1412, -9517, -5564, 2177, -1062, 2116,
           5309, 745, 134, 7804, 6195, -1529, -8924, 7449, 9926, -287, -5667, -1853, 924, -6439, 8176, -4671, 1309,
           -9027, -3902, 801, 1353, 9358, -3359, -8740, 8195, -6026, -6302, -1786, 7933, 1529, -1244, 1110, -5619,
           -4222, 5708, -7069, 4546, 3487, 6162, -5274, -4616, 676, 6636, -5461, -6940, -6921, -6026, -8602, -2027,
           -8636]
for amount in amounts:
    money = Money(amount)
    print('{}; {}'.format(+money, -money))
