"""
IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети.
IP-адреса представляют собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38.
Каждое число в наборе принадлежит интервалу от 0 до 255. Таким образом, полный диапазон
IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:

    ipaddress — IP-адрес, представленный в одном из следующих вариантов:

    строка из четырех целых чисел, разделенных точками
    список или кортеж из четырех целых чисел

Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:

IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')

И следующее неформальное строковое представление:

<IP-адрес в виде четырех целых чисел, разделенных точками>

Примечание 1. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса IPAddress нет, она может быть произвольной.
"""
from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, arg: str):
        self.ipaddress = arg

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, arg):
        self.ipaddress = ".".join(map(str, arg))

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"

    def __str__(self):
        return self.ipaddress


# INPUT DATA:

# TEST_1:
ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))

# TEST_2:
ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

# TEST_3:
ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))

# TEST_4:
addresses = [(189, 26, 106, 172), '97.248.190.45', '162.149.247.52', (160, 73, 135, 188), (216, 2, 39, 172),
             (31, 27, 97, 53), '95.233.16.231', (0, 19, 242, 236), (1, 166, 90, 22), '135.23.153.66', '235.99.24.247',
             '217.104.124.203', (99, 138, 21, 145), (231, 214, 91, 158), (158, 87, 228, 213), (32, 248, 59, 101),
             '244.236.12.239', '31.201.10.112', '68.206.225.207', '93.212.255.61']

for address in addresses:
    ip = IPAddress(address)
    print(repr(ip))
