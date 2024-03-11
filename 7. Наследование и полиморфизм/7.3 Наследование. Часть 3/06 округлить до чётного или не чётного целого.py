"""
Ближайшим четным числом для целого нечетного числа n будем считать n + 1, ближайшим четным числом для целого
    четного числа будет оно само. Аналогично ближайшим нечетным числом для целого четного числа n будем
    считать n + 1, ближайшим нечетным числом для целого нечетного числа будет оно само.

Реализуйте класс RoundedInt, наследника класса int, описывающий целое число, которое во время создания
    автоматически округляется до ближайшего четного или нечетного числа. При создании экземпляра класс
    должен принимать два аргумента в следующем порядке:

    num — объект, определяющий числовое значение экземпляра класса RoundedInt
    even — булево значение, определяющее четность при округлении. Если имеет значение True,
            округление происходит до ближайшего четного, если False — до ближайшего нечетного.
            По умолчанию имеет значение True

Примечание 1. Дополнительная проверка данных на корректность не требуется.
                Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса RoundedInt нет, она может быть произвольной.
"""


class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            return super().__new__(cls, num) if int(num) % 2 == 0 else super().__new__(cls, num + 1)
        else:
            return super().__new__(cls, num) if int(num) % 2 != 0 else super().__new__(cls, num + 1)


# INPUT DATA:

# TEST_1:
print("\nтест 1")
print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))

# TEST_2:
print("\nтест 2")
roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))

# TEST_3:
print("\nтест 3")
print(issubclass(RoundedInt, int))

# TEST_4:
print("\nтест 4")
for digit in range(100):
    print(RoundedInt(digit))

# TEST_5:
print("\nтест 5")
for digit in range(100):
    print(RoundedInt(digit, False))
