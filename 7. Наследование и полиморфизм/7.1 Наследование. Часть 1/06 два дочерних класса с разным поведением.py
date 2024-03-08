"""
1. Реализуйте класс Counter, описывающий неотрицательный счетчик. При создании экземпляра класс должен
    принимать один аргумент:

    start — начальное значение счетчика, по умолчанию равняется 0

Экземпляр класса Counter должен иметь один атрибут:

    value — текущее значение счетчика

Класс Counter должен иметь два метода экземпляра:

    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.
            Если число не передано, метод должен увеличить значение счетчика на единицу
    dec() — метод, принимающий в качестве аргумента целое число и уменьшающий значение счетчика на это число.
            Если число не передано, метод должен уменьшить значение счетчика на единицу. Значение счетчика
            считается равным 0, если при уменьшении оно становится отрицательным

2. Также реализуйте класс NonDecCounter, наследника класса Counter, описывающий счетчик, значение которого можно
    увеличивать, но нельзя уменьшать. Процесс создания экземпляра класса NonDecCounter должен совпадать с процессом
    создания экземпляра класса Counter.

Экземпляр класса NonDecCounter должен иметь один атрибут:

    value — текущее значение счетчика

Класс NonDecCounter должен иметь один метод экземпляра:

    dec() — пустой метод. Сигнатура метода должна совпадать с сигнатурой метода dec() класса Counter

3. Наконец, реализуйте класс LimitedCounter, наследника класса Counter, описывающий счетчик, значение которого можно
    увеличивать лишь до определенного числа. При создании экземпляра класс должен принимать два аргумента в следующем
    порядке:

    start — начальное значение счетчика, по умолчанию равняется 0
    limit — максимально возможное значение счетчика, по умолчанию равняется 10

Экземпляр класса LimitedCounter должен иметь один атрибут:

    value — текущее значение счетчика

Класс LimitedCounter должен иметь один метод экземпляра:

    inc() — метод, принимающий в качестве аргумента целое число и увеличивающий значение счетчика на это число.
            Если число не передано, метод должен увеличить значение счетчика на единицу. При увеличении значения
            счетчика метод не должен превышать установленный лимит

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


class NonDecCounter(Counter):
    def dec(self, reducer=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, magnifier=1):
        if self.value + magnifier >= self.limit:
            self.value = self.limit
        else:
            self.value += magnifier


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))

# TEST_2:
print("\nтест 2")
counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)

# TEST_3:
print("\nтест 3")
counter = NonDecCounter(10)

print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)

# TEST_4:
print("\nтест 4")
counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)

# TEST_5:
print("\nтест 5")
counter = LimitedCounter(limit=20)

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)

# TEST_6:
print("\nтест 6")
counter = LimitedCounter(start=5, limit=30)

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(24)
print(counter.value)

# TEST_7:
print("\nтест 7")
digits = [55, 40, 110, 183, 78, 181, 172, 158, 146, 35, 60, 180, 102, 170, 62, 46, 181, 68, 103, 124, 130, 127, 161,
          107, 199, 100, 74, 120, 132, 65, 167, 28, 45, 158, 53, 122, 86, 29, 199, 129, 97, 71, 113, 54, 134, 45, 76,
          157, 25, 60]

counter = Counter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)

# TEST_8:
print("\nтест 8")
digits = [105, 128, 149, 107, 119, 60, 60, 60, 188, 61, 154, 88, 161, 99, 199, 121, 77, 33, 185, 95, 182, 128, 166, 167,
          153, 115, 199, 124, 109, 65, 118, 20, 175, 194, 149, 184, 174, 162, 36, 51, 134, 196, 132, 129, 95, 199, 150,
          55, 123, 100]

counter = NonDecCounter(10)

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)

# TEST_9:
print("\nтест 9")
digits = [46, 158, 79, 100, 161, 100, 30, 27, 132, 79, 152, 114, 97, 171, 71, 35, 186, 157, 149, 144, 156, 41, 172, 122,
          131, 141, 69, 113, 86, 46, 104, 147, 42, 60, 31, 32, 190, 107, 110, 103, 77, 135, 35, 33, 104, 191, 94, 55,
          50, 156]

counter = LimitedCounter(start=10, limit=2000)

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)
