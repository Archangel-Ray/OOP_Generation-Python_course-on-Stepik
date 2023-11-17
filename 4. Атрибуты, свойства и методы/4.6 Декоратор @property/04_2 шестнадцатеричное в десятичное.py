"""
второй вариант. подглядел у ребят в правильных решениях. он не хранит дополнительную переменную,
но вычисляет её по запросу. вот даже не знаю что выгодней. высвобождаем оперативку, но нагружаем процессор.
"""


class Color:
    def __init__(self, arg):
        self.r = int()
        self.g = int()
        self.b = int()
        self.hexcode = arg

    @property
    def hexcode(self):
        return f'{hex(self.r)}{hex(self.g)}{hex(self.b)}'

    @hexcode.setter
    def hexcode(self, arg):
        self.r = int(arg[:2], 16)
        self.g = int(arg[2:4], 16)
        self.b = int(arg[4:], 16)


# INPUT DATA:

# TEST_1:
print('\nтест 1')
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_2:
print('\nтест 2')
color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_3:
print('\nтест 3')
color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print()

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

# TEST_4:
print('\nтест 4')
hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1
