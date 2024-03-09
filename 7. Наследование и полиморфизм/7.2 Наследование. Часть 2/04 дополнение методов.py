"""
Вам доступен класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс принимает один аргумент:

    start — начальное значение счетчика, по умолчанию равняется 0

Экземпляр класса Counter имеет один атрибут:

    value — текущее значение счетчика

Класс Counter имеет два метода экземпляра:

    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.
            Если число не передано, метод увеличивает значение счетчика на единицу
    dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число.
            Если число не передано, метод уменьшает значение счетчика на единицу. Значение счетчика считается
            равным 0, если при уменьшении оно становится отрицательным

Реализуйте класс DoubledCounter, наследника класса Counter, описывающий неотрицательный счетчик, значение которого
    увеличивается и уменьшается дважды при вызове соответствующих методов. Процесс создания экземпляра
    класса DoubledCounter должен совпадать с процессом создания экземпляра класса Counter.

Экземпляр класса DoubledCounter должен иметь один атрибут:

    value — текущее значение счетчика

Класс DoubledCounter должен иметь два метода экземпляра:

    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число дважды.
            Если число не передано, метод должен увеличить значение счетчика на два
    dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число дважды.
            Если число не передано, метод должен уменьшить значение счетчика на два. Значение счетчика считается
            равным 0, если при уменьшении оно становится отрицательным

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.
"""


class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, magnifier=1):
        self.value += magnifier

    def dec(self, reducer=1):
        if self.value - reducer <= 0:
            self.value = 0
        else:
            self.value -= reducer


class DoubledCounter(Counter):
    def inc(self, magnifier=1):
        super().inc(magnifier * 2)

    def dec(self, reducer=1):
        super().dec(reducer * 2)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(DoubledCounter, Counter))

# TEST_2:
print("\nтест 2")
counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

# TEST_3:
print("\nтест 3")
counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

# TEST_4:
print("\nтест 4")
digits = [47, 158, 163, 161, 65, 68, 56, 45, 66, 115, 20, 130, 108, 93, 144, 106, 106, 73, 67, 186, 158, 32, 49, 95,
          180, 169, 115, 64, 180, 163, 146, 143, 196, 143, 132, 184, 105, 38, 104, 174, 92, 169, 162, 38, 48, 29, 91,
          25, 145, 72]

counter = Counter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)

# TEST_5:
print("\nтест 5")
digits = [122, 48, 122, 180, 176, 148, 104, 70, 168, 128, 129, 120, 63, 172, 101, 132, 195, 139, 164, 163, 196, 132,
          110, 42, 183, 49, 50, 193, 198, 187, 172, 52, 113, 164, 196, 48, 114, 186, 78, 105, 82, 142, 97, 194, 74, 115,
          107, 160, 119, 82]

counter = DoubledCounter(10)

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)
