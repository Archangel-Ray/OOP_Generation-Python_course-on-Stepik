"""
Для кодирования цвета часто используется шестнадцатеричное значение цвета. Оно записывается в формате #RRGGBB,
где RR (красный), GG (зеленый) и BB (синий) являются шестнадцатеричными целыми числами в диапазоне [00; FF]
(или [0; 255] в десятичной системе счисления), которые указывают интенсивность соответствующих цветов.
Например, #0000FF представляет чистый синий цвет, так как синий компонент имеет наивысшее значение (FF),
а остальные — 00.

Реализуйте класс Color, описывающий цвет. При создании экземпляра класс должен принимать один аргумент:

    hexcode — шестнадцатеричное значение цвета

Экземпляр класса Color должен иметь три атрибута:

    r — интенсивность красного компонента цвета в виде десятичного числа
    g — интенсивность зеленого компонента цвета в виде десятичного числа
    b — интенсивность синего компонента цвета в виде десятичного числа

Класс Color должен иметь одно свойство:

    hexcode — свойство, доступное для чтения и записи, возвращающее шестнадцатеричное значение цвета

Примечание 1. При изменении шестнадцатеричного значения цвета значения атрибутов r, g и b также должны изменяться.

Примечание 2. Гарантируется, что для записи шестнадцатеричных чисел используются только заглавные латинские буквы.

Примечание 3. Дополнительная проверка данных на корректность не требуется.
              Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 4. Никаких ограничений касательно реализации класса Color нет, она может быть произвольной.
"""


class Color:
    def __init__(self, arg):
        self.r = int()
        self.g = int()
        self.b = int()
        self.hexcode = arg

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, arg):
        self._hexcode = arg
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
